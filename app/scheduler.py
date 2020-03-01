''' run apscheduler '''
# pylint: disable = invalid-name, missing-function-docstring
#   https://medium.com/better-programming/introduction-to-apscheduler-86337f3bb4a6
import logging
import time
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
import redlock
from . import APP, jobs


jobstores = {
    'default': RedisJobStore(host=APP.config.get('REDIS_HOST'), db=0)
}
SCHED = BlockingScheduler(jobstores=jobstores)


DLM = redlock.Redlock(APP.config.get('REDLOCK_CONN'))


# @SCHED.scheduled_job('interval', seconds=60)
def schedule_jobs():
    try:
        my_lock = DLM.lock('schedule_jobs', 10000)
        if my_lock:
            jobs.gen_report.queue()
            jobs.import_data.queue()
            jobs.send_emails.queue()
            jobs.update_cache.queue()
            jobs.recur_payment.queue()
            time.sleep(1)
            DLM.unlock(my_lock)
    except redlock.MultipleRedlockException as exc:
        logging.error(exc)
SCHED.add_job(schedule_jobs, 'interval', seconds=60)
