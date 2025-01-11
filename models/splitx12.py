from PIL import Image
import os
import math

def split_image_into_grid(image_path, num_splits=12):
    """Splits an image into a grid of approximately equal parts.

    Args:
        image_path: Path to the image file.
        num_splits: The desired number of splits.

    Returns:
        A list of paths to the saved grid parts.
    """

    original_image = Image.open(image_path)
    width, height = original_image.size

    # Calculate rows and columns based on desired splits and aspect ratio
    rows = int(math.sqrt(num_splits * (height / width)))  # Adjust rows based on aspect ratio
    cols = math.ceil(num_splits / rows)


    square_width = width // cols
    square_height = height // rows

    base_dir = os.path.dirname(image_path)
    output_dir = os.path.join(base_dir, f"grid_{rows}x{cols}")
    os.makedirs(output_dir, exist_ok=True)

    grid_parts = []

    for row in range(rows):
        for col in range(cols):
            left = col * square_width
            top = row * square_height
            right = min(left + square_width, width)  # Handle edge cases
            bottom = min(top + square_height, height) # Handle edge cases

            grid_part = original_image.crop((left, top, right, bottom))
            part_filename = f"grid_part_{row}_{col}.png"
            part_path = os.path.join(output_dir, part_filename)
            grid_part.save(part_path)
            grid_parts.append(part_path)
            
    print(f"Image split into {rows}x{cols} grid. Parts saved in {output_dir}")
    return grid_parts



def main():
    image_path = "27.jpg"  # Or your preferred name/path
    split_image_into_grid(image_path, num_splits=12)

if __name__ == "__main__":
    main()