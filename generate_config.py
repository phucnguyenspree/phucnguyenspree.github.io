import os
import json

# Path to your visualization_qc folder
root = "visualization_qc"

# Output file path
output_file = "categories.js"

categories = {}

for folder_name in sorted(os.listdir(root)):
    folder_path = os.path.join(root, folder_name)
    if not os.path.isdir(folder_path):
        continue

    categories[folder_name] = {"box": [], "polygon": []}

    for view_type in ["box", "polygon"]:
        view_path = os.path.join(folder_path, view_type)
        if not os.path.isdir(view_path):
            continue

        images = [
            f for f in sorted(os.listdir(view_path))
            if f.endswith(".png")
        ]
        categories[folder_name][view_type] = images

# Write the JavaScript file
with open(output_file, "w") as f:
    f.write("const categories = ")
    json.dump(categories, f, indent=2)
    f.write(";")
