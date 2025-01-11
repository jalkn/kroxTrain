from instagrapi import Client
import datetime
import time
import os

username = os.environ.get("INSTAGRAM_USERNAME")
password = os.environ.get("INSTAGRAM_PASSWORD")

client = Client()
client.login(username, password)

image_paths = [
    "quotes/1.jpg",
    "quotes/2.jpg",
    "quotes/3.jpg",
    "quotes/4.jpg",
    "quotes/5.jpg", 
]

caption = "My scheduled carousel caption"

# Scheduling the post for 3 hours from now


media_ids = []
for path in image_paths:
    media_id = client.photo_upload_to_story(path) 
    if media_id:
        media_ids.append(media_id)
    else:
        print(f"Failed to upload {path}")

if media_ids:
    client.album_upload(media_ids, caption=caption, publish_time=publish_time) #<- Add publish_time here
    print(f"Album scheduled successfully for {publish_time}!")
else:
    print("Failed to upload any images. Album not created.")