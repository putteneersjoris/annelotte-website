import os

# Define paths to files and directories
basedir = os.getcwd()
src_folder = os.path.join(basedir, "src")
actions_folder = os.path.join(basedir, ".github/workflows/")
file_paths = [
    os.path.join(actions_folder, "default.yaml"),
    os.path.join(src_folder, "index.html"),
    os.path.join(src_folder, "staticHtmlString.py"),
    os.path.join(src_folder, "generateData.py"),
    os.path.join(src_folder, "data.js"),
    os.path.join(src_folder, "script.js"),
    os.path.join(src_folder, "style.css")
]

# Function to read file content
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Generate README content using raw string
readme_content = r"""# Website: Annelotte Lammertse

## Stack:

Every push update (git cmd or GitHub web UI) triggers a GitHub Actions workflow that generates the static webpages.

### How:


```bash
Content of an update looks like this:


├── demoproject
│ ├── 1.jpg
│ ├── 2.jpg
│ ├── 3.jpg
│ ├── 4.jpg
│ ├── 5.jpg
│ └── description.txt

```


- 1 folder (demoproject) with images `1.jpg`, `2.jpg`, `3.jpg`, `4.jpg`, `5.jpg` (varying resolution, filesize is allowed. `.jpg`, `.png`, `.gif` are supported. also png transparency is supported)


### demoproject images
<div style="display: flex; flex-wrap: wrap;">
    <img src="./example/demoproject/1.jpg" width="32%">
    <img src="./example/demoproject/2.jpg" width="32%">
    <img src="./example/demoproject/3.jpg" width="32%">
    <img src="./example/demoproject/4.jpg" width="32%">
    <img src="./example/demoproject/5.jpg" width="32%">
</div>

re supported

- 1 `description.txt` file containing the following tags:
  - `<title>my_title*</title>`
  - `<date>11/2/2024*</date>`
  - `<body>main text**</body>`
  - `<tags>textile, weaving, digital*</tags>`

An example of hoz such a description.txt file


* --> all symbols are supported. this can be emoji's, spaces, underscores etc
** --> multiple tags a

```html


<title>Bioactive Textiles: Functionalization for Wound Healing and Healthcare</title>
<date>10/10/2024</date>
<tags>textile, bioactive, healthcare, wound healing</tags>
<body>
<h2>Project Overview</h2>
This project focuses on the development of bioactive textiles for applications in wound healing and healthcare. By incorporating bioactive agents into textile fibers, we aim to create functional textiles capable of promoting wound healing, preventing infections, and improving overall healthcare outcomes. The project involves a multidisciplinary approach that combines textile engineering, biomaterials science, and medical research to design innovative solutions for medical textiles.
The use of bioactive textiles has the potential to revolutionize wound care by providing continuous, localized delivery of therapeutic agents directly to the wound site. This targeted delivery system minimizes systemic side effects and enhances the efficacy of treatment. Additionally, bioactive textiles offer advantages such as improved patient comfort, reduced dressing changes, and simplified wound management procedures.  

The research objectives of the project include investigating methods for functionalizing textile fibers with bioactive agents, optimizing the release kinetics of therapeutic compounds, and evaluating the biocompatibility and safety of bioactive textiles for clinical use. Advanced fabrication techniques such as electrospinning, coating, and grafting will be employed to incorporate bioactive agents into textile matrices while preserving their structural integrity and mechanical properties.

<details><summary>Click for more details</summary>This section contains additional details about the project.
<a href="https://www.sciencedirect.com/science/article/pii/S014296121830642X">Read this paper</a>
<a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5799424/">Explore this study</a>
<a href="https://www.frontiersin.org/articles/10.3389/fbioe.2020.587592/full">Find out more</a> about advanced fabrication techniques for bioactive textiles.</details>
<details><summary>Click for more details</summary>This section contains additional details about the project.</details>

<p>The expected outcomes of the project include the development of bioactive textiles with tailored properties for specific medical applications, such as wound dressings, compression garments, and implantable devices. These innovative textiles have the potential to improve patient outcomes, reduce healthcare costs, and advance the field of regenerative medicine.</p>
</body>


```

this demoproject will render out on the website like this:

![header_image](./example/demoproject_1.png)
![header_image](./example/demoproject_2.png)

## how to upload?

```md

├── content
│   ├── ABOUT
│   │   ├── 068_Vtol_Murmansk_part2_PRMK__1340_c_670.jpg
│   │   ├── description2.txt
│   │   └── description.txt
│   ├── advanced textile composites
│   │   ├── 3_1340_c_670.jpg
│   │   ├── description.txt
│   │   └── DSC08966_1340_c_670.jpg
│   ├── bioactive textiles
│   │   ├── boo32m_670.jpg
│   │   ├── boom_670.jpg
│   │   ├── description.txt
│   │   ├── DSC03629_670.jpg
│   │   ├── vlcsnap-2020-07-27d-01h10m44s415_670.jpg
│   │   └── vlcsnap-2020-08-02-02h31m34s763_670.jpg
│   ├── demoproject
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   ├── 3.jpg
│   │   ├── 4.jpg
│   │   └── description.txt
│   ├── Digital Fabrication Techniques
│   │   ├── description.txt
│   │   └── Screen-Shot-2020-12-22-at-8.38.03-PM_670.png
│   ├── Smart Fabrics: Integrating Sensors for Health Monitoring
│   │   ├── 1_670.jpg
│   │   ├── 3_670.jpg
│   │   ├── 4_670.jpg
│   │   ├── 6_670.jpg
│   │   ├── 7_670.jpg
│   │   ├── 9_670.jpg
│   │   └── description.txt
│   └── sustainable dyeing techniques
│       ├── description.txt
│       ├── DSC03501_670.jpg
│       ├── DSC03513_670.jpg
│       └── DSC03526_670.jpg


```


1 go to the conternt folder located under annelotte_website/src/content/
2 click on "upload files" and drop your dolder
3 done







Once the content of this folder is final, we can upload it to the GitHub repository.

(If you are a student, you need to fork this first, The owner of the repository needs to approve it first)

GitHub Actions executes the commands in `./github/workflows/default.yaml` file. This includes copying all files to `gh-pages` branch, updating the Ubuntu instance, installing ImageMagick, updating Image
"""

for file_path in file_paths:
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        file_content = read_file_content(file_path)
        readme_content += f'\n\n<details><summary>{file_name}</summary>\n\n```\n{file_content}\n```\n</details>\n\n'

# Write README file
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("Readme generated successfully: README.md")
