import sys
import subprocess

def convert_avi_to_gif(input_file, output_file):
    ffmpeg_path = r'C:\FFmpeg\ffmpeg.exe'  # Replace with the actual path to your FFmpeg executable

    # Set the desired frame rate (frames per second)
    frame_rate = 15

    # Construct the FFmpeg command
    ffmpeg_command = [
        ffmpeg_path,
        '-i', input_file,
        '-r', str(frame_rate),
        '-c:v', 'gif',
        output_file
    ]

    # Execute the FFmpeg command
    subprocess.run(ffmpeg_command)

# Example usage: Convert AVI to GIF
if len(sys.argv) < 3:
    print("Usage: python script.py input_file output_file")
else:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_avi_to_gif(input_path, output_path)
