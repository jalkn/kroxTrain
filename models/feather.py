import turtle
import random
import math

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    turtle.bgcolor("black")
    t.pensize(1)
    return t

def draw_barb(t, length, angle, color1, color2):
    """Draw a single feather barb with gradient effect"""
    original_pos = t.position()
    original_heading = t.heading()
    
    # Draw main barb
    t.pencolor(color1)
    t.fillcolor(color2)
    t.begin_fill()
    
    # Create curved barb shape
    t.forward(length)
    t.right(angle)
    t.forward(length/4)
    t.right(angle)
    t.forward(length)
    t.right(180)
    
    t.end_fill()
    
    # Return to starting position
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)
    t.pendown()

def draw_feather_shaft(t, length, width):
    """Draw the main shaft of the feather"""
    t.pensize(width)
    t.pencolor("#8B4513")  # Brown color for shaft
    
    # Draw curved shaft
    t.right(5)
    for _ in range(length):
        t.forward(1)
        t.right(0.1)  # Slight curve

def generate_eagle_feather(length=400, barb_length=60):
    t = setup_turtle()
    turtle.tracer(0, 0)  # Turn off animation for speed
    
    # Color palette for eagle feather
    colors = [
        ("#4A3728", "#2C1810"),  # Dark brown
        ("#8B7355", "#6B5333"),  # Medium brown
        ("#D2B48C", "#BC9C7A"),  # Light brown/tan
        ("#F5DEB3", "#DEC49A"),  # Wheat
        ("#FFFFFF", "#F0F0F0"),  # White (for tips)
    ]
    
    # Starting position
    t.penup()
    t.goto(-length/2, 0)
    t.pendown()
    
    # Draw the main shaft
    draw_feather_shaft(t, length, 4)
    
    # Reset position for barbs
    t.penup()
    t.goto(-length/2, 0)
    t.setheading(0)
    
    # Draw barbs on both sides
    for side in [-1, 1]:  # -1 for left side, 1 for right side
        t.setheading(0)
        start_x, start_y = t.position()
        
        # Draw multiple layers of barbs
        for layer in range(3):  # Multiple layers for fuller appearance
            t.penup()
            t.goto(start_x, start_y)
            t.pendown()
            
            # Adjust angle based on side
            base_angle = 45 if side == 1 else 135
            t.setheading(base_angle)
            
            # Draw barbs along the shaft
            for i in range(length//10):
                x, y = t.position()
                
                # Vary barb length and angle for natural look
                current_length = barb_length * (1 - (i/length))
                angle_var = random.uniform(-5, 5)
                
                # Choose colors based on position
                color_pair = random.choice(colors)
                
                # Draw the barb
                draw_barb(t, current_length, 30 + angle_var, color_pair[0], color_pair[1])
                
                # Move to next position
                t.penup()
                t.goto(x + (10 * math.cos(math.radians(base_angle-90))),
                      y + (10 * math.sin(math.radians(base_angle-90))))
                t.pendown()
    
    # Add texture details
    t.pensize(1)
    for _ in range(50):
        x = random.randint(int(-length/2), int(length/2))
        y = random.randint(-barb_length, barb_length)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.pencolor("#D2B48C")
        t.circle(1)
    
    t.hideturtle()
    turtle.update()
    turtle.done()

# Generate eagle feather
# Parameters: length of feather, length of barbs
generate_eagle_feather(400, 60)