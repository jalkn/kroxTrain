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
        "slides": ["quotes/1.jpg, quotes/2.jpg, quotes/3.jpg, quotes/4.jpg"],
        "caption": "CYCLE01 RACE1 \n\n10 SETS:\n10 Burpees\n10 Box Jumps Over (20/24\")\n10 DB Snatch (17/22lbs)\nTime Cap: 25mins\n\nDiscipline is your silent companion on the path to greatness. When motivation fades, discipline carries you through. Keep pushing, keep growing. 🌱.\n.\n.\n.\n.\n.\n\n#KroxTrain #CycleOne #KroxRace #FunctionalFitness #DisciplineOverMotivation #CrossTraining #WorkoutOfTheDay #MentalToughness #TrainingDay #WorkoutChallenge #FitnessGoals #StrengthTraining #ConsistencyWins #DailyGrind",
        "hours_delay": 1
    }
    {
        "slides": ["quotes/5.jpg, quotes/6.jpg, quotes/7.jpg, quotes/8.jpg"],
        "caption": "Small steps every day create massive changes over time 💯 \n.\n.\n.\n #KroxTrain #ConsistencyIsKey #DailyProgress #FitnessLifestyle #ProgressNotPerfection #StayCommitted #WorkoutLife #FitnessMotivation #HealthyHabits #StrongBody #StrongMind #BuildingSuccess #KroxCommunity #TrainingDay #LifestyleChange",
        "hours_delay": 2
    },
    {
        "slides": ["quotes/9.jpg, quotes/10.png, quotes/11.png, quotes/12.png"], 
        "caption": "Every moment is a chance to start fresh. Your next chapter begins when you decide. Time to write your success story. 🔥 \n.\n.\n.\n#KroxTrain #NewBeginnings #StartNow #TransformationJourney #NoLimits #BreakBarriers #FitnessInspiration #PersonalGrowth #MakeItHappen #TakeAction #ChangeStartsNow #BelieveInYourself #KroxWarrior #FitLife #TimeForChange",
        "hours_delay": 3
    },
    {
        "slides": ["quotes/13.jpg, quotes/14.png, quotes/15.png, quotes/16.png"],
        "caption": "Nothing worth having comes easy. Every drop of sweat, every early morning, every extra rep - it all adds up to something extraordinary. 💪 \n.\n.\n.\n#KroxTrain #EarnedNotGiven #HardWorkPaysOff #StrengthInProgress #DedicationPays #ResultsDriven #WorkoutResults #FitnessAchievements #StrongerThanYesterday #GrindTime #SweatEquity #KroxResults #FitnessSuccess #TrainingGoals",
        "hours_delay": 4
    },
    {
        "slides": ["quotes/17.jpg, quotes/18.png, quotes/19.png, quotes/20.png"],
        "caption": "When you turn your passion into purpose, every workout becomes an investment in your future. Building more than just muscle - building legacy. 🎯 \n.\n.\n.\n#KroxTrain #PurposeDriven #BusinessMindset #FitnessEntrepreneur #BuildingLegacy #WorkoutBusiness #FitnessIndustry #SuccessMindset #KroxBusiness #EntrepreneurLife #FitnessLeader #IndustryStandards",
        "hours_delay": 5
    },
    {
        "slides": ["quotes/21.jpg, quotes/22.png, quotes/23.png, quotes/24.png"],
        "caption": "Your only real competition is the person you were yesterday. Every day is a chance to level up. Push your limits, break your barriers. 👊 \n.\n.\n.\n#KroxTrain #SelfImprovement #PersonalBest #CompeteWithYourself #BetterEveryDay #FitnessProgress #LevelUp #KroxAthlete #PersonalGoals #SelfMastery #ImprovementDaily #FitnessEvolution",
        "hours_delay": 24
    },
    {
        "slides": ["quotes/25.jpg, quotes/26.png, quotes/27.png, quotes/28.png"], 
        "caption": "This moment. This rep. This workout. This is where champions are made. Make every second count. ⚡ \n.\n.\n.\n#KroxTrain #PresentMoment #FocusedMindset #TrainingMoments #WorkoutFocus #IntensityMatters #KroxMomentum #TrainingDay #WorkoutTime #FitnessLife #TrainingZone #InTheMoment",
        "hours_delay": 48
    },
    {
        "slides": ["quotes/29.jpg, quotes/30.png, quotes/31.png, quotes/32.png"],  
        "caption": "Your mind will give up before your body does. Train both. Master both. Conquer your limits. 🧠💪 \n.\n.\n.\n #KroxTrain #MentalStrength #MindsetMatters #MentalToughness #PsychologyOfSuccess #MindBodyConnection #KroxMindset #MentalConditioning #StrongMind #MindOverMatter #MentalFitness",
        "hours_delay": 72
    },
    {
        "slides": ["quotes/33.jpg, quotes/34.png, quotes/35.png, quotes/36.png"],  
        "caption": "Find what sets your soul on fire. Chase it relentlessly. Let your passion fuel your progress. 🔥 \n.\n.\n.\n #KroxTrain #PassionDriven #PurposefulLiving #FitnessPassion #DedicatedLife #InspiredFitness #KroxPassion #LifeGoals #DreamChaser #PassionProject #LiveWithPurpose #InspirationalFitness",
        "hours_delay": 96
    },
    {
        "slides": ["quotes/37.jpg, quotes/38.png, quotes/39.png, quotes/40.png"],  
        "caption": "Build something worth remembering. Create a legacy that inspires. Your journey becomes someone else's guide. 👑 \n.\n.\n.\n #KroxTrain #LegacyBuilding #InspireGreatness #LeaveAMark #FitnessLegacy #KroxLegacy #BuildingDreams #InspireOthers #LeadByExample #CreateHistory #LastingImpact #FitnessLeader",
        "hours_delay": 120
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


