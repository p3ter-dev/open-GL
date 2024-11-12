import matplotlib.pyplot as plt

# Function to implement Liang-Barsky line clipping algorithm


def liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    t_enter = 0.0
    t_exit = 1.0

    for i in range(4):
        if p[i] == 0:  # Check if line is parallel to the clipping boundary
            if q[i] < 0:
                return None  # Line is outside and parallel, so completely discarded
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > t_enter:
                    t_enter = t
            else:
                if t < t_exit:
                    t_exit = t

    if t_enter > t_exit:
        return None  # Line is completely outside

    x1_clip = x1 + t_enter * dx
    y1_clip = y1 + t_enter * dy
    x2_clip = x1 + t_exit * dx
    y2_clip = y1 + t_exit * dy

    return x1_clip, y1_clip, x2_clip, y2_clip


# Define the clipping window
x_min, y_min = 20, 20
x_max, y_max = 80, 80

# Define the line (starting and ending points) - you can adjust these coordinates
x1, y1 = 10, 30
x2, y2 = 90, 60

# Apply the Liang-Barsky algorithm to clip the line
clipped_line = liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2)

# Plotting
plt.figure(figsize=(8, 6))

# Plot the clipping window
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min,
                                               y_max, y_max, y_min], 'b', label='Clipping Window')

if clipped_line is not None:
    x1_clip, y1_clip, x2_clip, y2_clip = clipped_line
    # Plot the original line
    plt.plot([x1, x2], [y1, y2], 'r', label='Original Line')
    # Plot the clipped line
    plt.plot([x1_clip, x2_clip], [y1_clip, y2_clip], 'g', label='Clipped Line')
    plt.title('Liang-Barsky Line Clipping Algorithm')
    plt.legend()
else:
    # The line is completely outside or parallel, so just plot the window
    plt.title('Line is outside the clipping window')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.axis('equal')
plt.show()
