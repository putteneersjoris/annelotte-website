import os

# Define paths to files and directories
basedir = os.getcwd()
src_folder = os.path.join(basedir, "src")
file_paths = [
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


- 1 folder (demoproject) with images (varying resolution, filesize is allowed. `.jpg`, `.png`, `.gif` are supported. also png transparency is supported)

* --> all symbols are supported. this can be emoji's, spaces, underscores etc
** --> multiple tags are supported

- 1 `.txt` file containing the following tags:
  - `<title>my_title*</title>`
  - `<date>11/2/2024*</date>`
  - `<body>main text**</body>`
  - `<tags>textile, weaving, digital*</tags>`

Once the content of this folder is final, we can upload it to the GitHub repository.

(If you are a student, you need to fork this first, The owner of the repository needs to approve it first)

GitHub Actions executes the commands in `./github/workflows/default.yaml` file. This includes copying all files to `gh-pages` branch, updating the Ubuntu instance, installing ImageMagick, updating Image
"""

for file_path in file_paths:
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        file_content = read_file_content(file_path)
        readme_content += f'\n\n<details open><summary>{file_name}</summary>\n\n```\n{file_content}\n```\n</details>\n\n'

# Write README file
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("Readme generated successfully: README.md")
