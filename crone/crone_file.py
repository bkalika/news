from crontab import CronTab
import os
full_path = os.path.dirname(os.path.abspath(__file__))

cron = CronTab(user=True)

job = cron.new(command=f"python3 {full_path}/delete_votes.py")

job.minute.every(1)
cron.write()
for job in cron:
    print(job)
