from instagrapi import Client
import schedule
import time
from datetime import datetime

def post_content(img_path, caption):
    try:
        username = "kroxtrain"
        password = ""  # Add password securely
        client = Client()
        client.login(username, password)
        
        client.photo_upload(img_path, caption=caption)
        print(f"[{datetime.now()}] Successfully posted: {img_path}")
        
    except Exception as e:
        print(f"[{datetime.now()}] Error posting {img_path}: {str(e)}")
    
    finally:
        try:
            client.logout()
        except:
            pass

def schedule_posts():
    # 5:00 AM - Morning Workout
    schedule.every().day.at("05:00").do(
        post_content,
        "quotes/1.jpg",
        "MORNING KROXTRAIN 🔥\nAdd weight each round when ready 💪\n#kroxtrain #morninggrind #trainharder"
    )
    
    # 10:00 AM - Progress Quote
    schedule.every().day.at("10:00").do(
        post_content,
        "quotes/2.jpg",
        "Progress demands patience.\nTrust the process.\nYour future self will thank you.\n#kroxtrain #motivation #growth"
    )
    
    # 3:00 PM - Afternoon Workout
    schedule.every().day.at("15:00").do(
        post_content,
        "quotes/3.jpg",
        "KROXTRAIN BEAST MODE 💪\nScale Options:\n- Reduce weight\n- Step-ups instead of jumps\n#kroxtrain #power #explosive #mindset #growth #noexcuses"
    )
    
    # 8:00 PM - Evening Motivation
    schedule.every().day.at("20:00").do(
        post_content,
        "quotes/4.jpg",
        "Stay locked in.\nYour goals don't care about excuses.\nKeep pushing forward. 💪\n#kroxtrain #motivation #growth"
    )

def main():
    print("Starting Instagram automation...")
    schedule_posts()
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        except Exception as e:
            print(f"Error in main loop: {str(e)}")
            time.sleep(300)  # Wait 5 minutes on error before retrying

if __name__ == "__main__":
    main()