import os
import json
import re
import subprocess


contentFolder = "./content"  # Specify the folder where your content is located
outputFolder = "./"     # Specify the folder where you want to save the HTML files


# Functions
def resize_file_if_large(filePath, maxBytes):
	file_size = os.path.getsize(filePath)
	command = f'convert "{filePath}" -resize 512x -quality 80 "{filePath}"'
	supported_extensions = (".jpg", ".png")
	if filePath.lower().endswith(supported_extensions):
		if file_size > maxBytes:
			print(f"{filePath} is too big with {file_size} bytes. It will be modified. Max bytes is {maxBytes}")
		if os.path.splitext(filePath)[1] == ".gif": # Check if GIF
			command = f'convert "{filePath}" -coalesce -resize 512x -colors 64 -deconstruct "{filePath}"'
		subprocess.run(command, shell=True)

def remove_unsupported_file(file_path):
	if os.path.isfile(file_path):
		supported_extensions = (".jpg", ".png", ".jpeg", ".txt", ".gif")
		if not file_path.lower().endswith(supported_extensions):
			os.remove(file_path)
			print(f'{file_path} is not supported and is removed. Please use one of the supported extensions {supported_extensions}')


#remove unsupported files
for folder in os.listdir(contentFolder):
	folder_path = os.path.join(contentFolder, folder)
	if os.path.isdir(folder_path):
		for item in os.listdir(folder_path):
			item_path = os.path.join(folder_path, item)
			remove_unsupported_file(item_path)



#resice images indeen needed
for folder in os.listdir(contentFolder):
	folder_path = os.path.join(contentFolder, folder)
	if os.path.isdir(folder_path):
		for item in os.listdir(folder_path):
			item_path = os.path.join(folder_path, item)
			# resize_file_if_large(item_path, 5000000)


# Delete all .html files (excluding index.html) in the output folder
for filename in os.listdir(outputFolder):
	filepath = os.path.join(outputFolder, filename)
	if filename.endswith(".html") and filename != "index.html":
		os.remove(filepath)
  

# Initialize arrays for images, tags, date, projects, allTags, and barContent
images = []
tags = []
date = []
projects = {}
allTags = []
barContent = []
htmlFiles = []

# make array with all projectnames
for folderName in os.listdir(contentFolder):
	folderPath = os.path.join(contentFolder, folderName)
	htmlFiles.append(folderName)

sorted_htmlFiles = sorted(htmlFiles)

# Iterate through the content folder
for i,folderName in enumerate(sorted(os.listdir(contentFolder))):
	# loop through sorted html_files so we can pick i+1 and i-1 fo to back and fort
	next_index = (i + 1) % len(sorted_htmlFiles)
	next_htmlFile = "./" + sorted_htmlFiles[next_index] + ".html"
	previous_index = (i - 1) % len(sorted_htmlFiles)
	previous_htmlFile = "./" + sorted_htmlFiles[previous_index] + ".html"

	folderPath = os.path.join(contentFolder, folderName)
	if os.path.isdir(folderPath):
		project_images = []
		project_tags = []
		project_date = []
		project_html = ""

		for item in os.listdir(folderPath):
			itemPath = os.path.join(folderPath, item)

			if os.path.isfile(itemPath):
				if item.endswith(".gif"):
					images.append(itemPath)
					project_images.append(itemPath)

				if item.endswith((".jpg", ".png")):
					itemPath_base = os.path.splitext(os.path.basename(itemPath))[0]
					itemPath_ext = os.path.splitext(os.path.basename(itemPath))[1]
					itemPath_resized = os.path.join(folderPath,itemPath_base + "_resized" + itemPath_ext)
					os.system(f'convert "{itemPath}"  -sharpen 0x.2 -resize x350 "{itemPath}"')
					images.append(itemPath)
					project_images.append(itemPath)

				elif item.endswith(".txt"):
					with open(itemPath, 'r') as txt_file:
						content = txt_file.read()
						date_match = re.search(r'<date>(.*?)<\/date>', content, re.DOTALL)
						if date_match:
							project_date.append(date_match.group(1).strip())
							project_date = date_match.group(1).strip()
						body_match = re.search(r'<body>(.*?)<\/body>', content, re.DOTALL)
						if body_match:
							project_html = body_match.group(1).strip()
							project_html = project_html.replace('\n', '<br>')
                        
						tags_match = re.search(r'<tags>(.*?)<\/tags>', content, re.DOTALL)
						if tags_match:
							tags_content = tags_match.group(1).strip()
							tags_formatted = ["#" + tag.strip() + "<br>" for tag in tags_content.split(',')]
							allTags.extend([
								"<span class='filter' data-filter='" + tag.strip() + "'>#" + tag.strip() + "</span>"
								for tag in tags_content.split(',')
							])
							# print(allTags)
		tag_list = [f"<span>#{tag.strip()}</span><br>" for tag in tags_content.split(",")]
		tag_string = "".join(tag_list)
		project_tags.append(tag_string)
		# print(project_tags)           
                
		project_images.sort()  # Sort the image paths for the current project
        
		projects[folderName] = {
			"images": project_images,
			"html": project_html,
			"tags": project_tags,
			"date": project_date
		}
        
		print(tags_content)
		# print(tags_content.replace(',','#'))


		# Create a project HTML file with images and barContent links
		images_html = "\n".join([f"<img class='imagesPage'  src='{image_path}' >" for image_path in project_images])
		
		project_html_content = f"""
			<!DOCTYPE html>
			<html lang="en">
					<head>
					<meta charset="UTF-8">
					<meta http-equiv="X-UA-Compatible" content="IE=edge">
					<meta name="viewport" content="width=device-width, initial-scale=1.0">
					<title>Annelotte Lammertse</title>
					<link rel="stylesheet" href="./style.css">
				</head>
				<body>
					<span id="tags-wrapper"></span> <!-- set tags here > -->
					<div id="header">
						<div id="title">
							<h1>
								<a href="./index.html" style="color: black; text-decoration: none;">Annelotte Lammertse</a>
							</h1>
						</div>
						<div id="bar">
							<div id="barContent"></div> <!-- set bar content projects here > -->
						</div>
						<div id="contentPage">
							<div id="textPage">
								<h1>{folderName} {project_date}</h1>  <!-- add back, next, and menu buttons here -->
								<div class="containerStatic">
									<div class="menuprevnext">
										<span>
											<a href='./index.html' class='backButtonPage'> menu</a>
										</span>
										<br>
										<span>
											<a href='{previous_htmlFile}' class='backButtonPage'>previous</a>
										</span>
										<br>
										<span>
											<a href= '{next_htmlFile}' class='backButtonPage'>next</a>
										</span>
									</div>
									<span id="tagStatic" style="color:rgb(0,0,0);">
										{tag_string}
									</span>
								</div>
								<body>
									<p>{project_html}</p>  <!-- body text here -->
								</body>
							</div>
							<div id="imagePage"> <!-- add all imiages here -->
								{images_html}
							</div>
						</div>
						<div id="footer">
							<span> Annelotte Lammertse </span>
							<span id="footerTextRight"></span>
						</div>
					</div>
				</body>

				<script src="data.js"></script> 
				<script src="script.js"></script> 
				
			
				<script>



document.addEventListener('DOMContentLoaded', function () {{
    // Apply fullscreen styles to images if less than 2 on startup; toggle on click otherwise
    const images = document.querySelectorAll('.imagesPage');
    images.forEach(img => {{
        img.addEventListener('click', () => {{
            img.classList.toggle('imagePageFull');
            img.style.width = img.classList.contains('imagePageFull') ? "100%" : "32.2%";
        }});
    }});

    if (images.length < 2) {{
        images.forEach(img => {{
            img.classList.add('imagePageFull');
            img.style.width = "100%";
        }});
    }}

    // Make the tags that are present red
    var tagsWrapper = document.getElementById('tags-wrapper');
    var tagStaticElements = document.getElementById('tagStatic').getElementsByTagName('span');
    var innerTagArray = [];
    for (var i = 0; i < tagStaticElements.length; i++) {{
        innerTagArray.push(tagStaticElements[i].innerHTML.replace('#', ''));
    }}

    var tags = tagsWrapper.getElementsByTagName('span');
    for (var i = 0; i < tags.length; i++) {{
        var dataFilter = tags[i].getAttribute('data-filter');
        if (innerTagArray.includes(dataFilter)) {{
            //tags[i].style.color = 'red';
            //tags[i].style.textDecoration = 'underline';
        }} else {{
            tags[i].style.color = 'rgb(200,200,200)';
            tags[i].style.textDecoration = 'line-through';
        }}
    }}
}});


				</script>
			</html>
		"""
		project_html_path = os.path.join(outputFolder, f"{folderName}.html")
		with open(project_html_path, 'w') as project_html_file:
			project_html_file.write(project_html_content)

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

# Write the JSON content to a file named "dataB.js"
with open("data.js", "w") as file:
	file.write("var content = ")
	file.write(content_json)

print("File 'dataB.js' saved successfully.")



























