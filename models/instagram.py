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

# Photo upload configuration
img1 = "quotes/1.jpg"  # morning workout
cap1 = "MORNING KROXTRAIN - Add weight each round when ready 💪 #kroxtrain #morninggrind #trainharder"

# Calculate publish time (3 hours from now)
now_utc = datetime.datetime.now(pytz.utc)
pub1 = now_utc + datetime.timedelta(hours=3)

# Upload photo
try:
    client.photo_upload(
        img1,
        caption=cap1,
        publish_time=pub1
    )
    logging.info("Photo uploaded successfully!")
except ClientError as e:
    logging.error(f"Photo upload failed: {e}")

img2 = "quotes/2.jpg" #Progress demands patience
cap2 = "Trust the process. Your future self will thank you. #kroxtrain #motivation #growth"
client.photo_upload(img2, caption=cap2)
print("Photo uploaded successfully!")

img3 = "quotes/3.jpg" #afternoon workout
cap3 = "KROXTRAIN BEAST MODE 💪 Scale Options: Reduce weight, Step-ups instead of jumps #kroxtrain #power #explosive #mindset #growth #noexcuses"
client.photo_upload(img3, caption=cap3)
print("Photo uploaded successfully!")

img4 = "quotes/4.jpg" #Stay locked in
cap4 = "Your goals don't care about excuses. Keep pushing forward. 💪 #kroxtrain #motivation #growth"
client.photo_upload(img4, caption=cap4)
print("Photo uploaded successfully!")

