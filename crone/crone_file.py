from crontab import CronTab

cron = CronTab(user=True)

job = cron.new(command="python3 /home/bohdan/Documents/work/news/crone/delete_votes.py")

job.minute.every(1)
cron.write()
for job in cron:
    print(job)
