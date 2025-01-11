from PIL import Image

def crop_to_square(image_path, output_path):

    try:
        img = Image.open(image_path)
        width, height = img.size

        # Determine the size of the square crop
        crop_size = min(width, height)

        # Calculate the coordinates for centering the crop
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
        right = left + crop_size
        bottom = top + crop_size

        # Perform the crop
        cropped_img = img.crop((left, top, right, bottom))

        # Save the cropped image
        cropped_img.save(output_path)
        print(f"Image cropped and saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:  # Handle other potential errors
        print(f"An error occurred: {e}")


# Example usage:
image_path = "../quotes/9.jpg"  # Replace with the actual path to your image
output_path = "../quotes/09.jpg" # Replace with desired output path
crop_to_square(image_path, output_path) 

