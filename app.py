from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()

@app.route("/")
def index():
    return "Welcome to the scheduler!"

def scheduledTask():
    print("This task is running every 5 seconds")
   

if __name__ == '__main__':
   # scheduler.add_job(id ='Scheduled task', func = scheduledTask, trigger = 'cron',day = "*", hour = 12, minute = 54)
    scheduler.add_job(id ='Scheduled task', func = scheduledTask, trigger = 'interval', seconds = 5)
    scheduler.start()
    app.run()
    
    
