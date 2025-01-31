import os
import datetime
from instagrapi import Client
from apscheduler.schedulers.blocking import BlockingScheduler

# Your Instagram credentials
USERNAME = os.environ.get("IG_USERNAME")  
PASSWORD = os.environ.get("IG_PASSWORD")

# Paths to your slide images/videos
MEDIA_PATHS = ["48.png",
               "49.png",
               "50.png",
               "51.png",
]

"""
.
Time Cap 18mins
6 Sets
9 Push ups
12 Kettlebell swings 20/24kg
15 Overhead lunges 20/24kg
.
.
.
Mobility, Hold for 1min
Dragon pose
Couch stretch
Lizard pose
Figure 4 stretch
World's greatest stretch
.
.
.
#crosstraining #fitness #crossfit #workout #gym #training #wod #motivation #fit #fitnessmotivation #sport #functionaltraining #crossfitgirls #personaltrainer #cardio #cross #weightlifting #crossfitlife #instafit #treino #saude #running #fitfam #coach #powerlifting #gymlife #crossfitbrasil #strength #crossfitter #bodybuilding
"""
# Your caption
CAPTION = '.\nTime Cap 25mins\n50-40-30-20-10\nWall Balls 14/20lbs\nKettlebell swings 20/24kg\nPull-ups\n.\n.\n.\nPush-ups\nAir squats\n.\n.\n.\n#crosstraining #fitness #crossfit #workout #gym #training #wod #motivation #fit #fitnessmotivation #sport #functionaltraining #crossfitgirls #personaltrainer #cardio #cross #weightlifting #crossfitlife #instafit #treino #saude #running #fitfam #coach #powerlifting #gymlife #crossfitbrasil #strength #crossfitter #bodybuilding'


def post_to_instagram():
    try:
        cl = Client()
        cl.login(USERNAME, PASSWORD)

        media_ids = []
        for path in MEDIA_PATHS:
            if path.endswith((".jpg", ".jpeg", ".png")):
                media_id = cl.photo_upload(path)
                media_ids.append(media_id.pk)
            elif path.endswith(".mp4"):
                media_id = cl.video_upload(path)
                media_ids.append(media_id.pk)

        cl.album_upload(media_ids, caption=CAPTION)


    except Exception as e:
        print(f"Error posting to Instagram: {e}")
    finally:
        cl.logout()



# Scheduling
scheduler = BlockingScheduler()

# Calculate the scheduled time (12 hours from now)
run_date = datetime.datetime.now() + datetime.timedelta(hours=11)

scheduler.add_job(post_to_instagram, 'date', run_date=run_date)

print(f"Post scheduled for {run_date}")
scheduler.start() 