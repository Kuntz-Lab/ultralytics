# loop through images in /tmp/train/images and compare to images in /tmp/val/images
# if an image is in val then we move it's label txt file to /tmp/val/labels and if the image is duplicated 
# in both directories then we delete the image from /tmp/train/images

import os
import shutil
from pathlib import Path

def remove_duplicate_images():
    # Define paths
    train_images_dir = Path('./tmp/train/images')
    train_labels_dir = Path('./tmp/train/labels')
    val_images_dir = Path('./tmp/val/images')
    val_labels_dir = Path('./tmp/val/labels')
    
    # Ensure all directories exist
    for directory in [train_images_dir, train_labels_dir, val_images_dir, val_labels_dir]:
        if not directory.exists():
            print(f"Directory {directory} does not exist.")
            return
    
    # Get lists of image files
    train_images = set(f.name for f in train_images_dir.glob('*.jpg'))
    val_images = set(f.name for f in val_images_dir.glob('*.jpg'))
    
    # Find duplicates (images that appear in both train and val)
    duplicates = train_images.intersection(val_images)
    
    print(f"Found {len(duplicates)} duplicate images")
    
    # Process each duplicate
    for image_name in val_images:
        # Get base name (without extension) for corresponding label file
        base_name = os.path.splitext(image_name)[0]
        label_file = f"{base_name}.txt"
        
        # Source and destination paths for label file
        src_label_path = train_labels_dir / label_file
        dst_label_path = val_labels_dir / label_file
        
        # Source path for image file
        src_image_path = train_images_dir / image_name
        
        # Check if the label file exists in train labels directory
        if src_label_path.exists():
            try:
                # Move the label file to val labels directory
                shutil.move(str(src_label_path), str(dst_label_path))
                print(f"Moved label: {label_file}")
                
                # Delete the image from train images directory
                if image_name in duplicates:
                    os.remove(str(src_image_path))
                    print(f"Removed image: {image_name}")
            except Exception as e:
                print(f"Error processing {image_name}: {e}")
        else:
            print(f"Warning: Label file {label_file} not found for {image_name}")

if __name__ == "__main__":
    remove_duplicate_images()
    print("Duplicate removal complete")