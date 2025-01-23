from PIL import Image

def change_background_color(input_path, output_path, target_color=(0, 0, 0)):
    """
    Change white background to specified color
    
    Args:
    input_path (str): Path to the input image
    output_path (str): Path to save the modified image
    target_color (tuple): RGB color to replace white background (default is black)
    """
    # Open the image
    img = Image.open(input_path).convert("RGBA")
    
    # Get image data
    data = img.getdata()
    
    # Create a new list to store modified pixel data
    new_data = []
    
    # Replace white background pixels
    for item in data:
        # If pixel is white (allowing some tolerance)
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            # Replace with target color while maintaining original alpha
            new_data.append(target_color + (item[3],))
        else:
            new_data.append(item)
    
    # Update image data
    img.putdata(new_data)
    
    # Save the modified image
    img.save(output_path)

# Example usage
change_background_color('models/races/0101/11.png', 'models/races/0101/17.png')