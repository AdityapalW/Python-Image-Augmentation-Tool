import cv2
import os
import random
import numpy as np

# Create output folder if not exists
output_folder = "augmented_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# List of augmentation transformations
def augment_image(image):
    augmented_images = []

    # Flip the image horizontally
    flipped_horiz = cv2.flip(image, 1)
    augmented_images.append(('flipped_horiz', flipped_horiz))

    # Rotate the image
    rows, cols = image.shape[:2]
    angle = random.randint(-30, 30)  # Random rotation angle
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    augmented_images.append(('rotated', rotated))

    # Scale the image
    scale_factor = random.uniform(0.7, 1.3)
    scaled = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    augmented_images.append(('scaled', scaled))

    # Random Crop
    x_start = random.randint(0, int(0.2 * cols))
    y_start = random.randint(0, int(0.2 * rows))
    cropped = image[y_start:y_start + int(0.8 * rows), x_start:x_start + int(0.8 * cols)]
    augmented_images.append(('cropped', cropped))

    return augmented_images

# Function to save augmented images
def save_augmented_images(image_path):
    image = cv2.imread(image_path)
    base_name = os.path.basename(image_path).split('.')[0]

    # Apply augmentations
    augmented_images = augment_image(image)

    for aug_name, aug_image in augmented_images:
        output_file = f"{output_folder}/{base_name}_{aug_name}.jpg"
        cv2.imwrite(output_file, aug_image)

# Main function to process images in a folder
def augment_images_in_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        save_augmented_images(image_path)
        print(f"Augmented images saved for {image_file}")

if __name__ == "__main__":
    input_folder = "input_images"  
    augment_images_in_folder(input_folder)
