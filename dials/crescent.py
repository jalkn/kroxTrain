import matplotlib.pyplot as plt
import numpy as np

def create_crescent(center_x, center_y, radius1, radius2, start_angle, end_angle):
    """Creates coordinates for a crescent shape."""
    theta = np.linspace(start_angle, end_angle, 500)  # Adjust 500 for smoothness
    x1 = center_x + radius1 * np.cos(theta)
    y1 = center_y + radius1 * np.sin(theta)
    x2 = center_x + radius2 * np.cos(theta)
    y2 = center_y + radius2 * np.sin(theta)

    x = np.concatenate([x1, x2[::-1]])  # Combine outer and inner arcs
    y = np.concatenate([y1, y2[::-1]])
    return x, y

# Circle parameters
center_x = 0
center_y = 0
radius_outer = 1.0
radius_middle = 0.7
radius_inner = 0.4

# Crescent parameters
start_angle = np.pi / 3  # Start at 90 degrees (top)
end_angle = 3 * np.pi / 2 # End at 270 degrees (bottom) 

# Create shapes
circle_outer_x = center_x + radius_outer * np.cos(np.linspace(0, 2*np.pi, 500))
circle_outer_y = center_y + radius_outer * np.sin(np.linspace(0, 2*np.pi, 500))


crescent1_x, crescent1_y = create_crescent(center_x, center_y, radius_middle, radius_inner, start_angle, end_angle)

# Second crescent (rotated 180 degrees)
crescent2_x, crescent2_y = create_crescent(center_x, center_y, radius_middle, radius_inner, start_angle + np.pi, end_angle + np.pi)  # Add pi to rotate


# Plot
fig, ax = plt.subplots()

ax.plot(circle_outer_x, circle_outer_y, color='black', linewidth=2) # Outer circle
ax.fill(crescent1_x, crescent1_y, color='black') # First crescent, filled
ax.fill(crescent2_x, crescent2_y, color='black')  # Second crescent, filled



# Set aspect ratio to equal for proper circle display
ax.set_aspect('equal')

# Remove axes
ax.axis('off')


plt.show()
