import os
import json

# Path to the directory containing the files
directory = "cocochanel-viz/subset_training/draw_images/"
coco_chanel_validation  = 'cocochanel-viz/subset_training/val_data_overfit.json'

parent = 'draw_images'
# Get the list of all files in the directory
files = os.listdir(directory)
#NOTE: Validation Set
# Open and read the JSON file
with open(coco_chanel_validation, 'r') as file:
    data = json.load(file)

# Create the HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 10px;
        }
        .image-container {
            margin: 5px;
            border: 1px solid #ccc;
            padding: 5px;
            border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            text-align: center;
            width: 250px; /* Smaller container width */
        }
        img {
            max-width: 250px; /* Smaller image width */
            height: auto;
            display: block;
            margin: 0 auto;
        }
        p {
            font-size: 12px; /* Smaller font size */
            margin: 5px 0 0;
        }
    </style>
</head>
<body>
    <h1>Subset Training overfit task1-4</h1>
"""

for id, file in enumerate(files):
    # Check if it's an image file
    caption = data[int(file.split('_')[0])]['conversations'][0]['content']
    file = os.path.join(parent, file)
    if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
        html_content += f"""
        <div class="image-container">
            <img src="{file}" alt="{file}">
            <p>{caption}</p>
        </div>
        """
    else:
        # For non-image files
        html_content += f"""
        <div class="image-container">
            <p>{id}</p>
        </div>
        """

html_content += """
</body>
</html>
"""

# Save the HTML file
output_file = "cocochanel-viz/subset_training/index.html"
with open(output_file, "w") as f:
    f.write(html_content)

print(f"HTML file created at {output_file}")
