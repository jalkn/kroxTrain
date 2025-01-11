from PIL import Image
import os

def split_image_into_grid(image_path, grid_size=4):

    # Open the image
    original_image = Image.open(image_path)
    
    # Get image dimensions
    width, height = original_image.size
    
    # Calculate the size of each grid square
    square_width = width // grid_size
    square_height = height // grid_size
    
    # Create output directory if it doesn't exist
    base_dir = os.path.dirname(image_path)
    output_dir = os.path.join(base_dir, f"grid_{grid_size}x{grid_size}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Store paths of created image parts
    grid_parts = []
    
    # Split the image into grid parts
    for row in range(grid_size):
        for col in range(grid_size):
            # Calculate the coordinates for cropping
            left = col * square_width
            top = row * square_height
            right = left + square_width
            bottom = top + square_height
            
            # Crop the image
            grid_part = original_image.crop((left, top, right, bottom))
            
            # Generate filename
            part_filename = f"grid_part_{row}_{col}.png"
            part_path = os.path.join(output_dir, part_filename)
            
            # Save the grid part
            grid_part.save(part_path)
            grid_parts.append(part_path)
    
    print(f"Image split into {grid_size}x{grid_size} grid. Parts saved in {output_dir}")
    return grid_parts

# Example usage
def main():
    # Replace with the path to your PNG image
    image_path = "27.jpg"
    
    # Optional: Specify grid size (default is 4x4)
    split_image_into_grid(image_path, grid_size=4)

if __name__ == "__main__":
    main()
