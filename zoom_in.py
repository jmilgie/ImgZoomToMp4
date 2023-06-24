import cv2
import os
import argparse

# Create parser
parser = argparse.ArgumentParser(description="Create zoom-in video from images.")
parser.add_argument('img_dir', type=str, help='Path to the image directory')
parser.add_argument('--playback_speed', type=float, default=2.0, help='Playback speed of the final video (lower is faster, default: 0.2)')

# Parse arguments
args = parser.parse_args()

# Use the arguments
img_dir = args.img_dir
playback_speed = args.playback_speed

# Specify video name
video_name = 'zoom_in_video.mp4'

# Get the list of all files in the directory
list_of_files = os.listdir(img_dir)

# Sort the files based on names so they're in the correct order
sorted_files = sorted(list_of_files)

# Empty list to hold images
images = []

for file in sorted_files:
    # Read image files and append to the list
    filepath = os.path.join(img_dir, file)
    images.append(cv2.imread(filepath))

# Get dimensions from the first image
height, width, layers = images[0].shape

# Choose the desired codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Get the original frame rate
original_frame_rate = 30

# Calculate the adjusted frame rate based on the playback speed
adjusted_frame_rate = original_frame_rate / playback_speed

# Create a new video writer with the adjusted frame rate
video = cv2.VideoWriter(video_name, fourcc, adjusted_frame_rate, (width, height))

# Specify how many frames for each zoom
zoom_frames = 90  # For example, 90 frames at 30 fps will create a 3-second zoom

def create_zoom_video(images, video, zoom_in=True):
    for i in range(len(images)):
        # Iterate through frames for each zoom
        for j in range(zoom_frames):
            # Calculate the scale for the current frame
            if zoom_in:
                scale = 1 + (2 - 1) * (j / zoom_frames)  # Gradually change scale from 1 to 2
            else:
                scale = 2 - (2 - 1) * (j / zoom_frames)  # Gradually change scale from 2 to 1

            # Calculate new dimensions
            new_width = int(width * scale)
            new_height = int(height * scale)

            # Resize the image
            resized_img = cv2.resize(images[i], (new_width, new_height))

            # Select the center of the resized image
            center_x = new_width // 2
            center_y = new_height // 2
            start_x = center_x - width // 2
            start_y = center_y - height // 2
            zoomed_img = resized_img[start_y:start_y + height, start_x:start_x + width]

            video.write(zoomed_img)

# Create zoom-in video
create_zoom_video(images, video, zoom_in=True)

# Copy and reverse images for zoom-out, exclude the last zoomed image
rev_images = images[:-1].copy()
rev_images.reverse()

# Add the first image of the reverse sequence at scale 1
rev_images.insert(0, images[-1])

# Begin zooming out with the new reversed list
create_zoom_video(rev_images, video, zoom_in=False)

# Release the video writer
video.release()

print("Video created successfully.")
