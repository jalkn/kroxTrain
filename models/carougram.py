from instagrapi import Client

username = ""
password = ""

client = Client()
client.login(username, password)

image_paths = [
    "quotes/1.jpg",
    "quotes/2.jpg",
    "quotes/3.jpg",
    "quotes/4.jpg",
    "quotes/5.jpg",  # Add paths to your 5 images
]

caption = "MORNING KROXTRAIN - Add weight each round when ready - Share your journey: @kroxtrain when you finish 💪 #kroxtrain #morninggrind #trainharder"

media_ids = []
for path in image_paths:
    media_id = client.photo_upload_to_story(path)  # Upload individually to get media IDs. Not adding to the story, just getting the IDs for the album.
    if media_id:
        media_ids.append(media_id)
    else:
        print(f"Failed to upload {path}")


if media_ids:  # Check if any uploads were successful
    client.album_upload(media_ids, caption=caption)
    print("Album uploaded successfully!")
else:
    print("Failed to upload any images. Album not created.")