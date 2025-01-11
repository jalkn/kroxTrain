from instagrapi import Client, ClientError
import datetime
import time
import os
import pytz
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Get credentials from environment variables
username = os.environ.get("INSTAGRAM_USERNAME")
password = os.environ.get("INSTAGRAM_PASSWORD")

# Initialize client
client = Client()

# Login to Instagram
try:
    client.login(username, password)
except ClientError as e:
    logging.error(f"Login failed: {e}")
    exit(1)

# Post configurations
posts = [
    {
        "image": "quotes/1.jpg", #morning workout
        "caption": "MORNING KROXTRAIN - Add weight each round when ready 💪 #kroxtrain #morninggrind #trainharder",
        "hours_delay": 1
    },
    {
        "image": "quotes/2.jpg", #Midday Quote. Progress demands patience
        "caption": "It's not about how fast you get there, but that you keep moving forward.  Embrace the journey, celebrate the small wins, and trust the process. 🔥#ProgressOverPerfection #PatienceIsKey #TrustTheProcess #KeepGoing #GrowthMindset #Motivation #JourneyToSuccess #SmallWins #NeverGiveUp #PositiveVibes #kroxtrain #motivation #growth",
        "hours_delay": 6
    },
    {
        "image": "quotes/3.jpg", #afternoon workout
        "caption": "KROXTRAIN BEAST MODE 💪 Scale Options: Reduce weight, Step-ups instead of jumps - Stay consistent, stay strong 💯 #kroxtrain #afternoongrind #dedication #kroxtrain #power #explosive #mindset #growth #noexcuses",
        "hours_delay": 11
    },
    {
        "image": "quotes/4.jpg", #Evening Quote. Discipline beats motivation
        "caption": "Discipline carries you when motivation fails. Keep pushing, keep growing 🌱 #kroxtrain #motivation #growth #eveningworkout #determination",
        "hours_delay": 16
    },
    {
        "image": "quotes/5.jpg", #morning workout
        "caption": "MORNING KROXTRAIN - Wake up, show up, crush it 🌅 #kroxtrain #morninggrind #trainharder",
        "hours_delay": 25
    },
    {
        "image": "quotes/6.jpg",  #earned not given
        "caption": "The struggle was real, but the reward is even sweeter. 💯 #earnednotgiven #challenges #overcome #strength #resilience #nevergiveup #fightforit #successstory #perseverance #determination #effort #results #proud #journey #growthmindset #noexcuses #kroxtrain #motivation #growth",
        "hours_delay": 30
    },
    {
        "image": "quotes/7.jpg",  #afternoon workout
        "caption": "KROXTRAIN BEAST MODE 💪 Scale Options:\n- 200m run\n- Single-unders\n - Lighter weight\n #kroxtrain #afternoongrind #dedication #kroxtrain #power #explosive #mindset #growth #noexcuses",
        "hours_delay": 35
    },
    {
        "image": "quotes/8.jpg",   #It's never too late
        "caption": "It's never too late to learn something new.  Whether it's a new skill, a new language, or a new perspective, embrace the journey of lifelong learning. 🌱 #kroxtrain #motivation #growth #eveningworkout #determination #NeverTooLate #LifelongLearning #Education #GrowthMindset #Curiosity #LearnSomethingNew #PersonalDevelopment #ExpandYourHorizons #NewSkills #KnowledgeIsPower",
        "hours_delay": 40
    }
]

# Calculate base time
now_utc = datetime.datetime.now(pytz.utc)

# Schedule and upload each post
for i, post in enumerate(posts, 1):
    try:
        # Calculate publish time
        publish_time = now_utc + datetime.timedelta(hours=post["hours_delay"])
        
        # Verify image exists
        if not os.path.exists(post["image"]):
            logging.error(f"Image not found: {post['image']}")
            continue
            
        # Upload photo
        client.photo_upload(
            post["image"],
            caption=post["caption"],
            publish_time=publish_time
        )
        logging.info(f"Post {i} scheduled successfully for {publish_time}")
        
        # Add a small delay between uploads to avoid rate limiting
        time.sleep(2)
        
    except ClientError as e:
        logging.error(f"Failed to schedule post {i}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error scheduling post {i}: {e}")

logging.info("All posts have been scheduled!")


