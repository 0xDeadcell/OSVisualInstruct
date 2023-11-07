import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import patches
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# Get the absolute path, where the script is located
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

# Load the Arial.ttf font
FONT_PATH = os.path.join(SCRIPT_PATH, 'Arial.ttf')
FONT_SIZE = 16
FONT = ImageFont.truetype(FONT_PATH, size=FONT_SIZE)

# Load the fresh screenshot
SCREENSHOT_PATH = os.path.join(SCRIPT_PATH, 'example_desktop_screenshot.png')
SCREENSHOT = Image.open(SCREENSHOT_PATH)
LABELED_OUTPUT_IMAGE_PATH = os.path.join(SCRIPT_PATH, 'grid_labeled_screenshot.png')

# Function to create and apply a grid with labels onto the screenshot
def create_grid_overlay(screenshot_path, div_factor=20, extend_top=50, extend_left=50):
    # Load the screenshot
    img = plt.imread(screenshot_path)
    
    # Create a figure and axes with an extended canvas
    dpi = 100  # Assuming 100 dots per inch for our figure
    fig_width = (img.shape[1] + extend_left) / dpi
    fig_height = (img.shape[0] + extend_top) / dpi
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi)
    # fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=dpi, facecolor='black')

    # Set the extent to shift the image on the canvas
    extent = [0, img.shape[1] + extend_left, img.shape[0] + extend_top, 0]

    # Display the image with 'upper' origin to have (0,0) at the top left
    ax.imshow(img, extent=extent, origin='upper')

    # # Calculate the grid lines positions
    # x_positions = np.arange(0, img.shape[1], img.shape[1] / (img.shape[1] // div_factor))
    # y_positions = np.arange(0, img.shape[0], img.shape[0] / (img.shape[0] // div_factor))

    # # Draw the grid lines
    # for pos in x_positions:
    #     ax.axvline(x=pos, color='red', linestyle='--', linewidth=0.5)
    # for pos in y_positions:
    #     ax.axhline(y=pos, color='red', linestyle='--', linewidth=0.5)

    # # Add the labels for the grid
    # for i, pos in enumerate(x_positions):
    #     rect = patches.Rectangle((pos-5, 0), 10, extend_top, linewidth=0)
    #     ax.add_patch(rect)
    #     ax.text(pos, extend_top + 25, str(int(pos)), color='white', ha='center', va='bottom', rotation=90, fontsize=FONT_SIZE)
    # for i, pos in enumerate(y_positions):
    #     rect = patches.Rectangle((0, pos-5), extend_left, 10, linewidth=0)
    #     ax.add_patch(rect)
    #     ax.text(extend_left + 10, pos, str(int(pos)), color='white', ha='right', va='center', fontsize=FONT_SIZE)

    # Adjust the subplot params
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    # Save the figure
    # Make the x,y increments every 50 pixels
    plt.xticks(np.arange(0, img.shape[1] + 50, 50))
    plt.yticks(np.arange(0, img.shape[0] + 20, 20))
    plt.grid(True)
    plt.savefig(LABELED_OUTPUT_IMAGE_PATH, bbox_inches='tight', pad_inches=0, dpi=dpi)
    #plt.savefig(LABELED_OUTPUT_IMAGE_PATH, bbox_inches='tight', pad_inches=0, dpi=dpi)

    return LABELED_OUTPUT_IMAGE_PATH

# Call the function to create the grid overlay
matplotlib_grid_output_path = create_grid_overlay(SCREENSHOT_PATH)
# Chunk image into 4 sections


# Open the image with the grid overlay
Image.open(matplotlib_grid_output_path).show()
