import os
import pandas as pd
import shutil

# Define paths
dataset_path = "dataset_v2"
csv_path = "labels_v2.csv"

# Read the CSV file
df = pd.read_csv(csv_path)

# Extract image paths from CSV
image_column = 'image_path'  # Adjust to match your CSV
df[image_column] = df[image_column].str.replace("dataset_v2/", "")  # Remove prefix if needed

# Create a mapping for images that actually exist
existing_images = sorted([f for f in os.listdir(dataset_path) if f.endswith('.jpg')])
existing_images_set = set(existing_images)

# Initialize mapping and new name counter
name_mapping = {}
new_index = 1025

# Track missing files
missing_files = []

for img_name in df[image_column]:
    if img_name in existing_images_set:
        new_name = f"image{new_index}.jpg"
        name_mapping[img_name] = new_name
        new_index += 1
    else:
        missing_files.append(img_name)

# First rename using temp names to avoid overwrite conflict
for old_name, new_name in name_mapping.items():
    old_path = os.path.join(dataset_path, old_name)
    temp_path = os.path.join(dataset_path, f"temp_{old_name}")
    shutil.move(old_path, temp_path)

# Then finalize the rename from temp to new name
for old_name, new_name in name_mapping.items():
    temp_path = os.path.join(dataset_path, f"temp_{old_name}")
    new_path = os.path.join(dataset_path, new_name)
    shutil.move(temp_path, new_path)

# Update CSV with new names (add prefix back)
df[image_column] = df[image_column].map(name_mapping).fillna(df[image_column])
df[image_column] = "dataset_v2/" + df[image_column]

# Save updated CSV
df.to_csv(csv_path, index=False)

print("✅ Renaming completed successfully!")
if missing_files:
    print("\n⚠️ Warning: The following files listed in CSV were not found in the folder:")
    for missing in missing_files:
        print(f"  - {missing}")
