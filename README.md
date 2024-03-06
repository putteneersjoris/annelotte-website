# website: Annelotte Lammertse



stack:

every push update (git cmd or github webui) 
triggers a github actions workflow that generates the statuc webpages


how:

content of an update looks like this:

├── demoproject
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   └── description.txt


- 1 folder (demoproject) with images (varying resolution,filesize is allowed. ".jpg",".png",".gif" are supported. also png transparancy is supported)

* --> all symbols are supported. this can be emoji's, spaces, underscores etc
** --> multiple tags are supported

- 1 .txt file containing the following tag
	<title>my_title*</title>
	<date>11/2/2024*</date> 
	<body>main text**</body>
	<tags>textile, weaving, digital*</tags>

once the content of this folder is final, we can upload it to the github repository.

(if you are a student, you need to fork this first, The owner of the reposity needs to approve it first)



github actions executes the commands in ./github/workflows/default.yaml file.
This includes copying all files to gh-pages branch
updating the ubuntu instance
installing imagemagick
updating imagemagick rights
executing generateData.py for the creation of the statuic webpages



```yaml
name: default
on:
  push:
    branches:
      - main
jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Set up ImageMagick
        run: |
          sudo apt-get update
          sudo apt-get install -y imagemagick
      - name: Update imagemagick rights Policy
        run: |
          sudo sed -i 's#<policy domain="path" rights="none" pattern="@\*"/>#<!-- <policy domain="path" rights="none" pattern="@*"/> -->#' /etc/ImageMagick-6/policy.xml
      - name: python generate data.js and html pages
        working-directory: src/
        run: python ./generateData.py
      - name: Deploy to Github Pages
        uses: crazy-max/ghaction-github-pages@v3
        with:
          target_branch: gh-pages
          build_dir: src
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


```

<details> <summary>python static html f-string </summary>

```py



  1 def html_string(folderName, project_date, previous_htmlFile, next_htmlFile, tag_string, project_html, images_html, num_images):
  2     project_html_content = f"""
  3 <!DOCTYPE html>
  4 <html lang="en">
  5 <head>
  6     <meta charset="UTF-8">
  7     <meta http-equiv="X-UA-Compatible" content="IE=edge">
  8     <meta name="viewport" content="width=device-width, initial-scale=1.0">
  9     <title>Annelotte Lammertse</title>
 10     <link rel="stylesheet" href="./style.css">
 11 </head>
 12 <body>
 13     <span id="tags-wrapper"></span> <!-- set tags here > -->
 14     <div id="header">
 15         <div id="title">
 16             <h1>
 17                 <a href="./index.html" style="color: black; text-decoration: none;">Annelotte Lammertse</a>
 18             </h1>
 19         </div>
 20         <div id="bar">
 21             <div id="barContent"></div> <!-- set bar content projects here > -->
 22         </div>
 23         <div id="contentPage">
 24             <div id="textPage">
 25                 <h1>{folderName} <br><span style="font-size:14px">{project_date}</span></h1>  <!-- add back, next, and menu buttons here -->
 26                 <div class="containerStatic">
 27                     <div class="menuprevnext">
 28                         <span>
 29                             <a href='./index.html' class='backButtonPage'> menu</a>
 30                         </span>
 31                         <br>
 32                         <span>
 33                             <a href='{previous_htmlFile}' class='backButtonPage'>previous</a>
 34                         </span>
 35                         <br>
 36                         <span>
 37                             <a href= '{next_htmlFile}' class='backButtonPage'>next</a>
 38                         </span>
 39                     </div>
 40                     <span id="tagStatic" style="color:rgb(0,0,0);">
 41                         {tag_string}
 42                     </span>
 43                 </div>
 44                 <body>
 45                     <p>{project_html}</p>  <!-- body text here -->
 46                 </body>
 47             </div>
 48             <div id="imagePage"> <!-- add all images here -->
 49                 {images_html}
 50             </div>
 51         </div>
 52         <div id="footer">
 53             <span> Annelotte Lammertse </span>
 54             <span id="footerTextRight"></span>
 55         </div>
 56     </div>
 57 </body>
 58 
 59 <script src="data.js"></script> 
 60 <script src="script.js"></script> 
 61 
 62 <script>
 63     document.addEventListener('DOMContentLoaded', function () {{
 64         // Apply fullscreen styles to images if less than 4 on startup; toggle on click otherwise
 65         const images = document.querySelectorAll('.imagesPage');
 66         images.forEach((img, index) => {{
 67             img.addEventListener('click', () => {{
 68                 img.classList.toggle('imagePageFull');
 69                 img.style.width = img.classList.contains('imagePageFull') ? "100%" : "32.2%";
 70             }});
 71 
 72             if (images.length < {num_images}) {{
 73                 img.classList.add('imagePageFull');
 74                 img.style.width = "100%";
 75             }} else if (images.length > {num_images} && index == 0) {{
 76                 img.classList.add('imagePageFull');
 77                 img.style.width = "100%";
 78             }}
 79         }});
 80 
 81         // Make the tags that are present red
 82         var tagsWrapper = document.getElementById('tags-wrapper');
 83         var tagStaticElements = document.getElementById('tagStatic').getElementsByTagName('span');
 84         var innerTagArray = [];
 85         for (var i = 0; i < tagStaticElements.length; i++) {{
 86             innerTagArray.push(tagStaticElements[i].innerHTML.replace('#', ''));
 87         }}
 88 
 89         var tags = tagsWrapper.getElementsByTagName('span');
 90         for (var i = 0; i < tags.length; i++) {{
 91             var dataFilter = tags[i].getAttribute('data-filter');
 92             if (innerTagArray.includes(dataFilter)) {{
 93                 tags[i].style.pointerEvents = 'none';
 94                 //tags[i].style.textDecoration = 'underline';
 95             }} else {{
 96                 tags[i].style.color = 'rgba(0,0,0,0.1)'
 97                 tags[i].style.textDecoration = 'line-through';
 98             }}
 99         }}
100     }});
101 </script>
102 </html>
103 """
104 
105     return project_html_content

```
</details>




<details> <summary>python file </summary>

```py
  1 import os
  2 import json
  3 import re
  4 import subprocess
  5 from staticHtmlString import html_string
  6 
  7 contentFolder = "./content"  # Specify the folder where your content is located
  8 outputFolder = "./"     # Specify the folder where you want to save the HTML files
  9 
 10 # Functions
 11 def resize_file_if_large(filePath, maxBytes):
 12 │       file_size = os.path.getsize(filePath)
 13 │       command = f'convert "{filePath}" -resize 512x -quality 80 "{filePath}"'
 14 │       supported_extensions = (".jpg", ".png")
 15 │       if filePath.lower().endswith(supported_extensions):
 16 │       │       if file_size > maxBytes:
 17 │       │       │       print(f"{filePath} is too big with {file_size} bytes. It will be modified. Max bytes is {maxBytes}")
 18 │       │       if os.path.splitext(filePath)[1] == ".gif": # Check if GIF
 19 │       │       │       command = f'convert "{filePath}" -coalesce -resize 512x -colors 64 -deconstruct "{filePath}"'
 20 │       │       subprocess.run(command, shell=True)
 21 
 22 def remove_unsupported_file(file_path):
 23 │       if os.path.isfile(file_path):
 24 │       │       supported_extensions = (".jpg", ".png", ".jpeg", ".txt", ".gif")
 25 │       │       if not file_path.lower().endswith(supported_extensions):
 26 │       │       │       os.remove(file_path)
 27 │       │       │       print(f'{file_path} is not supported and is removed. Please use one of the supported extensions {supported_extensions}')
 28 
 29 
 30 #remove unsupported files
 31 for folder in os.listdir(contentFolder):
 32 │       folder_path = os.path.join(contentFolder, folder)
 33 │       if os.path.isdir(folder_path):
 34 │       │       for item in os.listdir(folder_path):
 35 │       │       │       item_path = os.path.join(folder_path, item)
 36 │       │       │       remove_unsupported_file(item_path)
 37 
 38 
 39 
 40 #resice images indeen needed
 41 for folder in os.listdir(contentFolder):
 42 │       folder_path = os.path.join(contentFolder, folder)
 43 │       if os.path.isdir(folder_path):
 44 │       │       for item in os.listdir(folder_path):
 45 │       │       │       item_path = os.path.join(folder_path, item)
 46 │       │       │       # resize_file_if_large(item_path, 5000000)
 47 
 48 
 49 # Delete all .html files (excluding index.html) in the output folder
 50 for filename in os.listdir(outputFolder):
 51 │       filepath = os.path.join(outputFolder, filename)
 52 │       if filename.endswith(".html") and filename != "index.html":
 53 │       │       os.remove(filepath)
 54 
 55 
 56 # Initialize arrays for images, tags, date, projects, allTags, and barContent
 57 images = []
 58 tags = []
 59 date = []
 60 projects = {}
 61 allTags = []
 62 barContent = []
 63 htmlFiles = []
 64 
 65 # make array with all projectnames
 66 for folderName in os.listdir(contentFolder):
 67 │       folderPath = os.path.join(contentFolder, folderName)
 68 │       htmlFiles.append(folderName)
 69 
 70 sorted_htmlFiles = sorted(htmlFiles)
 71 
 72 # Iterate through the content folder
 73 for i,folderName in enumerate(sorted(os.listdir(contentFolder))):
 74 │       # loop through sorted html_files so we can pick i+1 and i-1 fo to back and fort
 75 │       next_index = (i + 1) % len(sorted_htmlFiles)
 76 │       next_htmlFile = "./" + sorted_htmlFiles[next_index] + ".html"
 77 │       previous_index = (i - 1) % len(sorted_htmlFiles)
 78 │       previous_htmlFile = "./" + sorted_htmlFiles[previous_index] + ".html"
 79 
 80 │       folderPath = os.path.join(contentFolder, folderName)
 81 │       if os.path.isdir(folderPath):
 82 │       │       project_images = []
 83 │       │       project_tags = []
 84 │       │       project_date = []
 85 │       │       project_html = ""
 86 
 87 │       │       for item in os.listdir(folderPath):
 88 │       │       │       itemPath = os.path.join(folderPath, item)
 89 
 90 │       │       │       if os.path.isfile(itemPath):
 91 │       │       │       │       if item.endswith(".gif"):
 92 │       │       │       │       │       images.append(itemPath)
 93 │       │       │       │       │       project_images.append(itemPath)
 94 
 95 │       │       │       │       if item.endswith((".jpg", ".png")):
 96 │       │       │       │       │       itemPath_base = os.path.splitext(os.path.basename(itemPath))[0]
 97 │       │       │       │       │       itemPath_ext = os.path.splitext(os.path.basename(itemPath))[1]
 98 │       │       │       │       │       itemPath_resized = os.path.join(folderPath,itemPath_base + "_resized" + itemPath_ext)
 99 │       │       │       │       │       os.system(f'convert "{itemPath}"  -sharpen 0x.2 -resize x350 "{itemPath}"')
100 │       │       │       │       │       images.append(itemPath)
101 │       │       │       │       │       project_images.append(itemPath)
102 
103 │       │       │       │       elif item.endswith(".txt"):
104 │       │       │       │       │       with open(itemPath, 'r') as txt_file:
105 │       │       │       │       │       │       content = txt_file.read()
106 │       │       │       │       │       │       date_match = re.search(r'<date>(.*?)<\/date>', content, re.DOTALL)
107 │       │       │       │       │       │       if date_match:
108 │       │       │       │       │       │       │       project_date.append(date_match.group(1).strip())
109 │       │       │       │       │       │       │       project_date = date_match.group(1).strip()
110 │       │       │       │       │       │       body_match = re.search(r'<body>(.*?)<\/body>', content, re.DOTALL)
111 │       │       │       │       │       │       if body_match:
112 │       │       │       │       │       │       │       project_html = body_match.group(1).strip()
113 │       │       │       │       │       │       │       project_html = project_html.replace('\n', '<br>')
114 
115 │       │       │       │       │       │       tags_match = re.search(r'<tags>(.*?)<\/tags>', content, re.DOTALL)
116 │       │       │       │       │       │       if tags_match:
117 │       │       │       │       │       │       │       tags_content = tags_match.group(1).strip()
118 │       │       │       │       │       │       │       tags_formatted = ["#" + tag.strip() + "<br>" for tag in tags_content.split(',')]
119 │       │       │       │       │       │       │       allTags.extend([
120 │       │       │       │       │       │       │       │       "<span class='filter' data-filter='" + tag.strip() + "'>#" + tag.strip() + "</span>"
121 │       │       │       │       │       │       │       │       for tag in tags_content.split(',')
122 │       │       │       │       │       │       │       ])
123 │       │       │       │       │       │       │       # print(allTags)
124 │       │       │       │       │       #break out of the loop after procvessing the first file
125 │       │       │       │       │       break
126 │       │       tag_list = [f"<span>#{tag.strip()}</span><br>" for tag in tags_content.split(",")]
127 │       │       tag_string = "".join(tag_list)
128 │       │       project_tags.append(tag_string)
129 │       │       # print(project_tags)           
130 
131 │       │       project_images.sort()  # Sort the image paths for the current project
132 
133 │       │       projects[folderName] = {
134 │       │       │       "images": project_images,
135 │       │       │       "html": project_html,
136 │       │       │       "tags": project_tags,
137 │       │       │       "date": project_date
138 │       │       }
139 
140 │       │       print(tags_content)
141 │       │       # print(tags_content.replace(',','#'))
142 
143 
144 │       │       # Create a project HTML file with images and barContent links
145 │       │       images_html = "\n".join([f"<img class='imagesPage'  src='{image_path}' >" for image_path in project_images])
146 │       │       num_images = 4│ 
147 │       │       
148 │       │       #html string comes from staticHtmlString
149 │       │       project_html_content = html_string(folderName, project_date, previous_htmlFile, next_htmlFile, tag_string, project_html, images_html, num_images)
150 
151 
152 
153 │       │       project_html_path = os.path.join(outputFolder, f"{folderName}.html")
154 │       │       with open(project_html_path, 'w') as project_html_file:
155 │       │       │       project_html_file.write(project_html_content)
156 
157 allTags = list(set(allTags))
158 allTags.sort()
159 
160 # Sort the project names
161 sorted_project_names = sorted(projects.keys())
162 
163 # Create the barContent array with formatted project names
164 formatted_barContent = [
165 │       "<a href='./" + project_name + ".html'>" + project_name + "</a>&ensp;&ensp;"
166 │       for project_name in sorted_project_names
167 ]
168 
169 # Duplicate the formatted_barContent array 10 times
170 duplicated_barContent = formatted_barContent * 10
171 
172 # Create the content dictionary with sorted projects
173 sorted_projects = {project_name: projects[project_name] for project_name in sorted_project_names}
174 
175 # Create the content dictionary
176 content = {
177 │       "projects": sorted_projects,
178 │       "allTags": allTags,
179 │       "barContent": duplicated_barContent
180 }
181 
182 # Convert the content dictionary to JSON format
183 content_json = json.dumps(content, indent=4)
184 
185 # Write the JSON content to a file named "dataB.js"
186 with open("data.js", "w") as file:
187 │       file.write("var content = ")
188 │       file.write(content_json)
189 
190 print("File 'dataB.js' saved successfully.")
191 
192 
193 
194 
195 

```
</details>




<details> <summary>javascript file script.js </summary>

```js


  1 var PIXELDISTANCE = 4
  2 
  3 
  4 var projectsData = content.projects;
  5 
  6 var barData = "";
  7 // var allTagsDataArray = content.allTags
  8 var barArray = content.barContent;
  9 for (var i = 0; i < barArray.length; i++) {
 10   barData += barArray[i];
 11 }
 12 document.getElementById('barContent').innerHTML = barData
 13 
 14 
 15 // set tags
 16 var allTagsData = "";
 17 var allTagsDataArray =  content.allTags
 18 for (var i = 0; i < allTagsDataArray.length; i++) {
 19     allTagsData += allTagsDataArray[i];
 20 }
 21 
 22 // Get the tags-wrapper element and set its innerHTML
 23 
 24 
 25 document.getElementById('tags-wrapper').innerHTML = "<span id='all' style='text-decoration:underline;'>#all<br><br><br></span>"  +  allTagsData;
 26 
 27 // Loop over each project in the "projects" object
 28 for (var projectName in content.projects) {
 29   if (content.projects.hasOwnProperty(projectName)) {
 30       var project = content.projects[projectName];
 31   }
 32 }
 33 
 34 var nProjects = 0
 35 for (var projectName in content.projects) {
 36   if (content.projects.hasOwnProperty(projectName)) {
 37       var project = content.projects[projectName];
 38       nProjects +=1
 39       // Create a <span> tag
 40 │       var spanTag = document.createElement("span");
 41 │       spanTag.classList.add("project")
 42 │       spanTag.style.zIndex = 100-nProjects
 43 │       spanTag.setAttribute("data-tags", project.tags.join(" "));
 44 
 45 │       var imgATag = document.createElement("a");
 46 │       imgATag.href = projectName + ".html"
 47 │       var imgTag = document.createElement("img");
 48 │       imgTag.src = project.images[0];
 49 
 50 │       imgATag.appendChild(imgTag)
 51 │       spanTag.appendChild(imgATag);
 52 
 53 
 54 │       // Create an <a> tag with project.html as href
 55 │       var aTag = document.createElement("a");
 56 │       aTag.href = projectName + ".html";
 57 │       var divEndImg = document.createElement("div");
 58 │       divEndImg.classList.add("endImg");
 59 │       // aTag.style
 60 
 61 │       var divProjectName = document.createElement("div");
 62 │       divProjectName.classList.add("projectName");
 63 │       divProjectName.textContent = projectName;
 64 
 65 
 66 │       var divProjectDate = document.createElement("div");
 67 │       divProjectDate.classList.add("projectDate");
 68 │       divProjectDate.textContent = project.date;
 69 
 70 │       // Create the <div> element with class "projectTags"
 71 │       var divProjectTags = document.createElement("div");
 72 │       divProjectTags.classList.add("projectTags");
 73 │       divProjectTags.innerHTML = project.tags
 74 
 75 │       divEndImg.appendChild(divProjectName);
 76 │       divEndImg.appendChild(divProjectDate);
 77 │       divEndImg.appendChild(divProjectTags);
 78 │       aTag.appendChild(divEndImg);
 79 
 80 │       spanTag.appendChild(aTag);
 81 
 82 │       var projectsTag = document.getElementById("projects")
 83 
 84 │       projectsTag.appendChild(spanTag);
 85 │       }
 86 }
 87 
 88 
 89 // Get the div with id "projects"
 90 const projectsDiv = document.getElementById("projects");
 91 
 92 // Define a function to update the width of the elements based on the div's width
 93 function updateWidth() {
 94     // Get the current width of the div
 95     const width = projectsDiv.offsetWidth;
 96    console.log(width)
 97     // Calculate the width for each "project" class
 98     const n_projects = 5;
 99     const dist = (Math.floor(width / n_projects) - 3) + "px";
100 
101     // Set the width for each "project" class
102     const projectElements = document.getElementsByClassName('project');
103     for (let i = 0; i < projectElements.length; i++) {
104         let imgTags = projectElements[i].getElementsByTagName('img');
105         for (let j = 0; j < imgTags.length; j++) {
106             imgTags[j].style.width = dist;
107             imgTags[j].style.height = dist;
108         }
109     }
110 
111     // Set the width for each element with class "endImg"
112     const projectElementsImg = document.getElementsByClassName('endImg');
113     for (let i = 0; i < projectElementsImg.length; i++) {
114         projectElementsImg[i].style.width = dist;
115         projectElementsImg[i].style.height = dist;
116     }
117 }
118 
119 // Call updateWidth initially to set the initial width
120 updateWidth();
121 
122 // Add a resize event listener to the window object to call updateWidth whenever the window is resized
123 window.addEventListener('resize', updateWidth);
124 
125 
126 // set date on footer
127 var currentDate = new Date
128 var year = currentDate.getFullYear()
129 document.getElementById('footerTextRight').innerHTML = "@" + year
130 
131 
132 const filters = document.querySelectorAll('.filter');
133 const projects = document.querySelectorAll('.project');
134 const all = document.getElementById('all');
135 let selectedFilters = [];
136 
137 all.addEventListener("click", function() {
138     var styleAttr = all.getAttribute("style");
139 
140     if (!styleAttr || styleAttr.indexOf('text-decoration: none') === -1) {
141         all.style.textDecoration = "none";
142         console.log("Set all projects to hidden");
143         projects.forEach(project => {
144             project.classList.add('hidden');
145         });
146     } else {
147         all.style.textDecoration = "underline";
148         console.log("Revealing all projects");
149         projects.forEach(project => {
150             project.classList.remove('hidden');
151         });
152         filters.forEach(filter => {
153             filter.classList.remove('selected');
154         });
155     }
156 });
157 
158 filters.forEach(filter => {
159     filter.addEventListener('click', () => {
160         const filterValue = filter.getAttribute('data-filter');
161         const isSelected = selectedFilters.includes(filterValue);
162 
163         // Toggle the selected state
164         if (isSelected) {
165             const index = selectedFilters.indexOf(filterValue);
166             selectedFilters.splice(index, 1);
167             filter.classList.remove('selected');
168         } else {
169             selectedFilters.push(filterValue);
170             filter.classList.add('selected');
171         }
172 
173         // Check if "all" is selected
174         const allSelected = selectedFilters.includes('all');
175 
176         projects.forEach(project => {
177             const tags = project.getAttribute('data-tags');
178             if (allSelected || selectedFilters.every(tag => tags.includes(tag))) {
179                 project.classList.remove('hidden');
180             } else {
181                 project.classList.add('hidden');
182             }
183         });
184 
185         // Check if no filters are selected and display message
186         if (selectedFilters.length === 0) {
187             all.style.textDecoration = "underline";
188         } else {
189             all.style.textDecoration = "none";
190         }
191     });
192 });
193 



```

</details>





<details> <summary>index.html file </summary>



```html


  1 <!DOCTYPE html>
  2 <html lang="en">
  3 <head>
  4     <meta charset="UTF-8">
  5     <meta http-equiv="X-UA-Compatible" content="IE=edge">
  6     <meta name="viewport" content="width=device-width, initial-scale=1.0">
  7     <title>Annelotte</title>
  8     <link rel="stylesheet" href="style.css">
  9 </head>
 10 
 11 <body>
 12 │       <span id="tags-wrapper"></span> <!-- set tags here > -->
 13 │       <div id="header">
 14 │       │       <div id="title">
 15 │       │       │       <h1><a href="./index.html" style="color: black; text-decoration: none;">Annelotte Lammertse</a></h1>
 16 │       │       </div>
 17 │       │       <div id="bar">
 18 │       │       │       <div id="barContent"></div> <!-- set bar content projects here > -->
 19 │       │       </div>
 20 │       │        <div id="content">
 21 │       │       │       <div id="projects"></div>
 22 │       │       </div>
 23 │       </div>
 24 │       <div id="footer">
 25 │       │       <span> Annelotte Lammertse </span><span id="footerTextRight"></span>
 26 │       </div>
 27 </body>
 28 
 29 <script src="data.js"></script>
 30 <script src="script.js"></script>
 31 </html>
 32 


```

</details>








