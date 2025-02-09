import os
import shutil
import random
from tqdm import tqdm

# Base path where your dataset is stored
DATASET_PATH = r"E:\07-12_yolo\data"  # Update this to your actual dataset folder

# Output directories for images and labels
OUTPUT_PATH = r"E:\07-12_yolo\ha"
IMG_FOLDER = os.path.join(OUTPUT_PATH, "images")
LABEL_FOLDER = os.path.join(OUTPUT_PATH, "labels")

# Define train, val, test subdirectories
splits = ["train", "val", "test"]
split_ratios = {"train": 0.7, "val": 0.2, "test": 0.1}

# Create necessary directories
for split in splits:
    os.makedirs(os.path.join(IMG_FOLDER, split), exist_ok=True)
    os.makedirs(os.path.join(LABEL_FOLDER, split), exist_ok=True)

# Ensure dataset path exists
if not os.path.exists(DATASET_PATH):
    print(f"❌ Error: Dataset path '{DATASET_PATH}' does not exist.")
    exit()

# Get all unique image names (without extensions)
image_files = sorted([f for f in os.listdir(DATASET_PATH) if f.endswith(('.jpg', '.png'))])
base_filenames = [os.path.splitext(f)[0] for f in image_files]

# Shuffle dataset
random.seed(42)
random.shuffle(base_filenames)

# Calculate split sizes
total_files = len(base_filenames)
train_count = int(total_files * split_ratios["train"])
val_count = int(total_files * split_ratios["val"])
test_count = total_files - train_count - val_count  # Remaining files for test

# Split the dataset
split_data = {
    "train": base_filenames[:train_count],
    "val": base_filenames[train_count:train_count + val_count],
    "test": base_filenames[train_count + val_count:]
}

# Function to copy images and labels
def copy_files(file_list, split_name):
    for base_name in tqdm(file_list, desc=f"Processing {split_name} set"):
        img_src = os.path.join(DATASET_PATH, base_name + ".png")  # Change extension if needed
        txt_src = os.path.join(DATASET_PATH, base_name + ".txt")  # TXT labels

        img_dest = os.path.join(IMG_FOLDER, split_name, base_name + ".png")
        txt_dest = os.path.join(LABEL_FOLDER, split_name, base_name + ".txt")

        if os.path.exists(img_src):
            shutil.copy2(img_src, img_dest)
        else:
            print(f"⚠ Warning: Image {img_src} not found.")

        if os.path.exists(txt_src):
            shutil.copy2(txt_src, txt_dest)
        else:
            print(f"⚠ Warning: Label {txt_src} not found. Creating empty label file.")
            open(txt_dest, "w").close()  # Create empty file if label is missing

# Copy files into train, val, and test folders
for split in splits:
    copy_files(split_data[split], split)

print("🎉 Dataset split and copied successfully!")