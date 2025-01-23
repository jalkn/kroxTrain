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
        "slides": ["quotes/54.jpg, quotes/55.png, quotes/56.png, quotes/57.png"],
        "caption": "CYCLE 01 RACE 06\nTime Cap 20mins:\n- 15 Burpees\n- 50 Double-unders\n- 20 Kettlebell swings 20/24kg\n.\n.\n.\nDesliza para tu dosis diaria de poder:\n① Crosstraining\n② Movilidad\n③ Mentalidad del día 💭\n.#kroxtrain #entrenamiento #fitness #crosstraining #fuerza #disciplina #constancia #motivacion #gimnasio #ejercicio #vidasana #entreno #fitnessmotivacion #fuerzamental #noexcusas #ganasdefitness #crossfit #comunidadfitness #estilodevida #sinlimites \n.\n.\n.\n#KroxTrain #EarnedNotGiven #HardWorkPaysOff #StrengthInProgress #DedicationPays #ResultsDriven #WorkoutResults #FitnessAchievements #StrongerThanYesterday #GrindTime #SweatEquity #KroxResults #FitnessSuccess #TrainingGoals",
        "hours_delay": 5
    }
]

# Function to upload album (multiple photos/slides)
def upload_album(caption, paths, publish_time):
    media_ids = []
    for path in paths:
        if not os.path.exists(path):
            logging.error(f"Image not found: {path}")
            return None  # Stop if any image is missing
        try:
            media_id = client.photo_upload_to_story(path) # Upload to story first to get media_id
            media_ids.append(media_id)
        except Exception as e:
            logging.error(f"Error uploading slide: {e}")
            return None
    try:
      client.album_upload(
          media_ids,
          caption=caption,
          publish_time=publish_time
      )
      return True
    except Exception as e:
      logging.error(f"Error uploading album: {e}")
      return None
  
# Calculate base time
now_utc = datetime.datetime.now(pytz.utc)

# Schedule and upload each post (now handling albums/slides)
for i, post in enumerate(posts, 1):
    publish_time = now_utc + datetime.timedelta(hours=post["hours_delay"])

    if upload_album(post["caption"], post["slides"], publish_time):
        logging.info(f"Post {i} (album) scheduled successfully for {publish_time}")
    else:
        logging.error(f"Failed to schedule post {i}")

    time.sleep(2)  # Delay between uploads


logging.info("Finished scheduling posts!")


