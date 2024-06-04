import os
import shutil
import random

# Configuration
main_dir = '/home/hp/dataset4/dataset'
labeled_dir = '/home/hp/dataset4/labeled'
unlabeled_dir = '/home/hp/dataset4/unlabeled'
labeled_ratio = 0.10  # 10% labeled

# Step 1: Create directories for labeled and unlabeled data
os.makedirs(labeled_dir, exist_ok=True)
os.makedirs(unlabeled_dir, exist_ok=True)

total_images = 0
total_unlabeled = 0  # Track total number of unlabeled images added

subdirs = ['airfield', 'canyon', 'temple', 'market', 'bus-stand']
for subdir in subdirs:
    subdir_path = os.path.join(main_dir, subdir)
    images = os.listdir(subdir_path)
    total_images += len(images)

num_labeled_total = int(total_images * labeled_ratio)
num_unlabeled_total = total_images - num_labeled_total

print(f"Total number of images: {total_images}")
print(f"Number of labeled images: {num_labeled_total}")
print(f"Number of unlabeled images: {num_unlabeled_total}")

# Function to copy images and handle filename conflicts
def copy_image(src, dst_dir):
    base_name = os.path.basename(src)
    dst = os.path.join(dst_dir, base_name)
    counter = 1
    while os.path.exists(dst):
        name, ext = os.path.splitext(base_name)
        dst = os.path.join(dst_dir, f"{name}_{counter}{ext}")
        counter += 1
    shutil.copy(src, dst)

# Iterate over each subdirectory
for subdir in subdirs:
    subdir_path = os.path.join(main_dir, subdir)
    images = os.listdir(subdir_path)
    
    # Shuffle the images to randomize the selection
    random.shuffle(images)
    
    # Calculate the number of labeled and unlabeled images
    num_labeled = int(len(images) * labeled_ratio)
    num_unlabeled = len(images) - num_labeled
    
    # Track total number of unlabeled images added
    total_unlabeled += num_unlabeled
    
    print(f"Subdirectory: {subdir}")
    print(f"Total images: {len(images)}")
    print(f"Number of labeled images: {num_labeled}")
    print(f"Number of unlabeled images: {num_unlabeled}")
    
    # Split the images into labeled and unlabeled
    labeled_images = images[:num_labeled]
    unlabeled_images = images[num_labeled:]
    print(f"Number of labeled images after splitting: {len(labeled_images)}")
    print(f"Number of unlabeled images after splitting: {len(unlabeled_images)}")
    
    # Create subdirectories in labeled directory
    labeled_subdir = os.path.join(labeled_dir, subdir)
    os.makedirs(labeled_subdir, exist_ok=True)
    
    # Step 2: Copy the labeled images to the respective subdirectory
    for img in labeled_images:
        shutil.copy(os.path.join(subdir_path, img), os.path.join(labeled_subdir, img))
        
    # Step 3: Copy the unlabeled images to the unlabeled directory (no subdirectories)
    for img in unlabeled_images:
        copy_image(os.path.join(subdir_path, img), unlabeled_dir)

print(f"Total number of unlabeled images added: {total_unlabeled}")
print(f"Labeled data saved to {labeled_dir}")
print(f"Unlabeled data saved to {unlabeled_dir}")

# Verify the number of files in the unlabeled directory
num_unlabeled_images = len(os.listdir(unlabeled_dir))
print(f"Total number of unlabeled images in the folder: {num_unlabeled_images}")