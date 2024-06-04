import os
import shutil
from glob import glob
import math

# Define the paths
base_dir = 'D:\Study\COMP 6721\Project\COMP6721-project\Dataset'
train_dir = os.path.join(base_dir, 'Train')
test_dir = os.path.join(base_dir, 'Test')
val_dir = os.path.join(base_dir, 'Validation')

# Create Test and Validation directories
print("Creating Test and Validation directories...")
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Iterate through each subfolder in Train
print("Processing subfolders in Train directory...")
for subdir in os.listdir(train_dir):
    sub_train_dir = os.path.join(train_dir, subdir)
    if os.path.isdir(sub_train_dir):
        sub_test_dir = os.path.join(test_dir, subdir)
        sub_val_dir = os.path.join(val_dir, subdir)
        
        # Create corresponding subfolders in Test and Validation
        print(f"Creating subfolders for {subdir} in Test and Validation directories...")
        os.makedirs(sub_test_dir, exist_ok=True)
        os.makedirs(sub_val_dir, exist_ok=True)
        
        # List all images in the current subfolder
        images = glob(os.path.join(sub_train_dir, '*'))
        print(f"Found {len(images)} images in {sub_train_dir}")
        
        # Calculate the number of images to move
        num_images = len(images)
        num_test = math.ceil(num_images * 0.2)
        num_val = math.ceil(num_images * 0.2)
        
        # Move images to Test folder
        print(f"Moving {num_test} images from {sub_train_dir} to {sub_test_dir}...")
        for i in range(num_test):
            shutil.move(images[i], sub_test_dir)
        
        # Move images to Validation folder
        print(f"Moving {num_val} images from {sub_train_dir} to {sub_val_dir}...")
        for i in range(num_test, num_test + num_val):
            shutil.move(images[i], sub_val_dir)

print("Dataset splitting completed.")