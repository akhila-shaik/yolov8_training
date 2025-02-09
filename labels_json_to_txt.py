import json
import os

# Define the folder containing JSON files
json_folder = r"E:\07-12_yolo\data\annotations\json"
output_folder = r"E:\07-12_yolo\data\annotations\labels_op/"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Define class mapping (Modify as needed)
class_mapping = {"object": 0}  

# Process each JSON file in the folder
for json_file in os.listdir(json_folder):
    if json_file.endswith(".json"):
        json_path = os.path.join(json_folder, json_file)

        # Load JSON annotation
        with open(json_path, "r") as f:
            data = json.load(f)

        # Extract image size
        img_width = data["imageWidth"]
        img_height = data["imageHeight"]

        # Process each shape
        yolo_annotations = []
        for shape in data["shapes"]:
            label = shape["label"]
            if label not in class_mapping:
                continue  # Skip unknown classes
            
            class_id = class_mapping[label]

            # Get bounding box coordinates
            x_min = shape["points"][0][0]
            y_min = shape["points"][0][1]
            x_max = shape["points"][2][0]
            y_max = shape["points"][2][1]

            # Convert to YOLO format
            x_center = ((x_min + x_max) / 2) / img_width
            y_center = ((y_min + y_max) / 2) / img_height
            width = (x_max - x_min) / img_width
            height = (y_max - y_min) / img_height

            yolo_annotations.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

        # Save to .txt file (same name as image but .txt extension)
        txt_filename = os.path.splitext(json_file)[0] + ".txt"
        txt_path = os.path.join(output_folder, txt_filename)
        
        with open(txt_path, "w") as f:
            f.write("\n".join(yolo_annotations))

        print(f"Converted {json_file} → {txt_filename}")

print("Conversion completed for all JSON files!")

