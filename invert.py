from PIL import Image, ImageOps

def invert_png_color(input_path, output_path=None):

    # Open the image
    with Image.open(input_path) as img:
        # Ensure the image is in RGB mode
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Invert the colors
        inverted_img = ImageOps.invert(img)
        
        # Determine output path
        if output_path is None:
            # Insert '_inverted' before the file extension
            parts = input_path.rsplit('.', 1)
            output_path = f"{parts[0]}_inverted.{parts[1]}"
        
        # Save the inverted image
        inverted_img.save(output_path)
        
        return output_path

# Example usage
if __name__ == "__main__":
    # Simple example of inverting an image
    try:
        # Invert an image and save with default naming
        inverted_image_path = invert_png_color('fav.png')
        print(f"Inverted image saved to: {inverted_image_path}")
        
        # Invert an image and specify a custom output path
        custom_inverted_path = invert_png_color('fav.png', 'inverted.png')
        print(f"Custom inverted image saved to: {custom_inverted_path}")
    
    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")