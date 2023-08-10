import os
import json
import re

contentFolder = "./content"  # Specify the folder where your content is located
outputFolder = "./output"     # Specify the folder where you want to save the HTML files

# Create the output folder if it doesn't exist
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Initialize arrays for images, tags, date, projects, allTags, and barContent
images = []
tags = []
date = []
projects = {}
allTags = []
barContent = []

# Iterate through the content folder
for folderName in os.listdir(contentFolder):
    folderPath = os.path.join(contentFolder, folderName)
    if os.path.isdir(folderPath):
        project_images = []
        project_tags = []
        project_date = []
        project_html = ""
        
        for item in os.listdir(folderPath):
            itemPath = os.path.join(folderPath, item)
            
            if os.path.isfile(itemPath):
                if item.endswith((".jpg", ".png")):
                    images.append(itemPath)
                    project_images.append(itemPath)
                elif item.endswith(".txt"):
                    with open(itemPath, 'r') as txt_file:
                        content = txt_file.read()
                        date_match = re.search(r'<date>(.*?)<\/date>', content, re.DOTALL)
                        if date_match:
                            project_date.append(date_match.group(1).strip())
                        
                        body_match = re.search(r'<body>(.*?)<\/body>', content, re.DOTALL)
                        if body_match:
                            project_html = body_match.group(1).strip()
                        
                        tags_match = re.search(r'<tags>(.*?)<\/tags>', content, re.DOTALL)
                        if tags_match:
                            tags_content = tags_match.group(1).strip()
                            tags_formatted = ["#" + tag.strip() + "<br>" for tag in tags_content.split(',')]
                            project_tags.append(''.join(tags_formatted))
                            # Add each tag to the allTags array
                            allTags.extend([
                                "<span class='filter' data-filter='" + tag.strip() + "'>#" + tag.strip() + "</span>"
                                for tag in tags_content.split(',')
                            ])
        
        project_images.sort()  # Sort the image paths for the current project
        
        projects[folderName] = {
            "images": project_images,
            "html": project_html,
            "tags": project_tags,
            "date": project_date
        }
        

        
        # Create a project HTML file with images and barContent links
        images_html = "\n".join([f"<img src='{image_path}' alt='{os.path.basename(image_path)}'>" for image_path in project_images])
        project_html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{folderName}</title>
</head>
<body>
    <h1>{folderName}</h1>
    <p>{project_html}</p>
    {images_html}
    
    <hr>
    <h2>Bar Content Links</h2>
</body>
</html>
"""
        project_html_path = os.path.join(outputFolder, f"{folderName}.html")
        with open(project_html_path, 'w') as project_html_file:
            project_html_file.write(project_html_content)

# Sort and deduplicate allTags array
allTags = list(set(allTags))
allTags.sort()

# Sort the project names
sorted_project_names = sorted(projects.keys())

# Create the barContent array with formatted project names
formatted_barContent = [
    "<a href='./" + project_name + ".html'>" + project_name + "</a>&ensp;&ensp;"
    for project_name in sorted_project_names
]

# Duplicate the formatted_barContent array 10 times
duplicated_barContent = formatted_barContent * 10

# Create the content dictionary with sorted projects
sorted_projects = {project_name: projects[project_name] for project_name in sorted_project_names}

# Create the content dictionary
content = {
    "projects": sorted_projects,
    "allTags": allTags,
    "barContent": duplicated_barContent
}

# Convert the content dictionary to JSON format
content_json = json.dumps(content, indent=4)

# Print the JSON object
print(content_json)

# Write the JSON content to a file named "dataB.js"
with open("data.js", "w") as file:
    file.write("var content = ")
    file.write(content_json)

print("File 'dataB.js' saved successfully.")