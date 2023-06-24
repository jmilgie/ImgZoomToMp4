# ImgZoomToMp4

ImgZoomToMp4 is a Python-based tool that takes a series of zoomed images and stitches them together to create a zoom-in/zoom-out video. Optionally, you can convert the resulting video into a GIF file.

## Prerequisites

Before running the scripts, you need to ensure that you have Python and FFmpeg installed on your system. You can download Python from [here](https://www.python.org/downloads/) and FFmpeg from [here](https://www.ffmpeg.org/download.html).

This project also requires the following Python packages:

- `cv2` (OpenCV)
- `argparse`
- `os`
- `sys`
- `subprocess`

You can install them using pip:

```bash
pip install opencv-python
```

Note: The other modules (`argparse`, `os`, `sys`, `subprocess`) are part of the Python Standard Library and do not need to be installed separately.

## Running the Scripts

### zoom_in.py

This script creates a zoom-in and zoom-out video from a sequence of images.

To run the script, use the following command:

```bash
python zoom_in.py /path/to/your/image/directory --playback_speed 2.0
```

This will create a zoom in/out video named `zoom_in_video.mp4` in the same directory where the script is executed.

The script accepts two command-line arguments:

- `img_dir` (required): Path to the directory containing your images.
- `--playback_speed` (optional): Playback speed of the final video. Lower values will make the video play faster. The default is 2.0.

### avi_to_gif.py

This script converts an AVI video file into a GIF file. It requires FFmpeg to work.

To run the script, use the following command:

```bash
python avi_to_gif.py /path/to/your/input.avi /path/to/your/output.gif
```

This will convert the `input.avi` file into a GIF file named `output.gif`.

The script accepts two command-line arguments:

- `input_file` (required): Path to the input AVI file.
- `output_file` (required): Path to the output GIF file.

## Contributing

Pull requests are welcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Please ensure that you replace the FFmpeg path in `avi_to_gif.py` with the path to your actual FFmpeg executable.
