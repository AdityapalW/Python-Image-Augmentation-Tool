# Image Augmentation Tool

This Python script allows you to apply basic image transformations like flipping, rotating, scaling, and cropping. It's useful for expanding datasets in image processing tasks.

## Features
- Flip images horizontally
- Rotate images randomly between -30 to +30 degrees
- Scale images between 70% and 130%
- Crop random sections of the images

## Requirements
You need to have **Python 3.x** installed along with the following libraries:
- **OpenCV** (for image processing)
- **NumPy** (for handling arrays and calculations)

You can install these by running:

```bash
pip install opencv-python numpy
```

## How to Use

1. **Place your images** in a folder called `input_images`.
2. **Run the script** with Python:
   ```bash
   python3 script.py
   ```
3. The transformed images will be saved in a new folder called `augmented_images`.

### Example Command:
```bash
python3 script.py
```

## Folder Structure

```
project-folder/
│
├── script.py              # The main Python script
├── input_images/          # Your folder for input images
├── augmented_images/      # The folder where the augmented images will be saved
└── README.md              # This README file
```

## Example Output
The script will save images with names like:
- `image_flipped_horiz.jpg`
- `image_rotated.jpg`
- `image_scaled.jpg`

