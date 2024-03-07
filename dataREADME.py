#README content using raw string

admin = "Annelotte"
admin_fullname = "Annelotte Lammertse"
user = "student"
admin_github_account = "https://github.com/AnnelotteLammertse"
admin_repository_name = "annelottelammertse"

user_github_account = "https://github.com/studentName"
user_repository_name = "annelottelammertse"

# videos and images
# admin
admin_only_once = "./example/admin_only_once.gif"
admin_upload_project = "./example/admin_upload_project.gif"
admin_update_project = "./example/admin_update_project.gif"
admin_remove_project = "./example/admin_remove_project.gif"
admin_approve_project = "./example/admin_approve_project.gif"

admin_confirmation_email = "./example/admin_confirmation_email.jpg"

# user
user_only_once = "./example/user_only_once.gif"
user_fork_repository = "./example/user_fork_repository.gif"
user_update_project = "./example/user_update_project.gif"
user_upload_project = "./example/user_upload_project.gif"
user_remove_project = "./example/user_remove_project.gif"

# naviagtion
menu_navigation = "./example/manu_navigation.png"
project_navigation = "./example/project_navigation.png"

#admin
admin_setup = f""" 

# Website: {admin_fullname}

## Uploading, Updating, Removing, Confirming Projects

First setup ({admin}) (only once)

Make sure you have a GitHub account: [{admin_github_account}]({admin_github_account})

Setup the repository so it has correct GitHub actions, bot permissions, etc.
The original repository can be found [here](https://github.com/putteneersjoris/{admin_repository_name}).


# Website: {admin_fullname}

## Uploading, Updating, Removing, Confirming Projects

### First setup ({admin}) (only once)

1. Make sure you have a GitHub account: [{{admin_github_account}}]({{admin_github_account}})

2. Setup the repository so it has correct GitHub actions, bot permissions, etc.
   - The original repository can be found [here](https://github.com/putteneersjoris/{{admin_repository_name}}).
"""

admin_upload_project = f"""
<details><summary>1. How do I ({admin}) upload projects?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to the content directory ({admin_github_account}/{admin_repository_name}/tree/main/src/content).
│   You can upload a project by simply dragging and dropping your project folder into GitHub, or by navigating to 'Add file' > 'Upload files'.
│   ![Upload Project]({admin_upload_project})
│   You have successfully uploaded a project. You can preview updates in 'Incognito mode' in your browser. Keep in mind that your browser caches content, so updates may be delayed for some time.
</details>

 """
admin_remove_project = f""" <details><summary>2. How do I ({admin}) remove projects?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to the content directory ({admin_github_account}/{admin_repository_name}/tree/main/src/content).
│   ![Remove Project]({admin_remove_project})
│   You have successfully removed a project. You can preview updates in 'Incognito mode' in your browser. Keep in mind that your browser caches content, so updates may be delayed for some time.
</details>

"""
admin_update_project = f""" <details><summary>3. How do I ({admin}) update a project?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to the content directory ({admin_github_account}/{admin_repository_name}/tree/main/src/content).
│   In the following video, it shows how to update the description as well as removing and adding images.
│   ![Update Project]({admin_update_project})
│   You have successfully updated a project. You can preview updates in 'Incognito mode' in your browser. Keep in mind that your browser caches content, so updates may be delayed for some time.
</details>

"""
admin_approve_project = f""" <details><summary>4. How do I ({admin}) approve a student project?</summary>
│   Option 1: Approve the pull requests of the {user} as shown in the video.
│   │   ![Approve Project]({admin_approve_project})
│       
│   Option 2: You will receive an email from GitHub regarding an update.
│   │   ![Confirmation Email]({admin_confirmation_email}) You can approve the {user} project by clicking the provided link.
│   
│   You have successfully confirmed a project. You can preview updates in 'Incognito mode' in your browser. Keep in mind that your browser caches content, so updates may be delayed for some time.
</details>

"""


#user
user_setup = f""" First setup ({user}) (only once)
Make sure you have a GitHub account.
Fork the repository located under {admin}'s repository [here](https://github.com/AnnelotteLammertse/annelottelammertse) as demonstrated in this [video]({user_fork_repository}).

"""
user_upload_project = f""" <details><summary>1. How do I ({user}) upload a project?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to your instance of {admin}'s website located at ({user_github_account}/{user_repository_name}).
│   Sync fork (this makes sure you have the latest version so there are no conflicts between other users).
│   Go to the content folder: ({user_github_account}/{user_repository_name}/tree/main/src/content).
│   You can upload a project by simply dragging and dropping your project folder into GitHub, or by navigating to 'Add file' > 'Upload files'.
│   Upload your project as shown in the following video.
│   ![Upload Project]({user_upload_project})
│   
│   Contribute by opening up a 'pull request > create pull request'.
│   Now {admin} will get an email notification, as well as having an open pull request that can be approved or disapproved.
│   You now have successfully uploaded a project. Once {admin} approves of the changes, you can see your project on the official website.
</details>

"""
user_remove_project = f""" <details><summary>3. How do I ({user}) remove a project?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to your instance of {admin}'s website located at ({user_github_account}/{user_repository_name}).
│   Sync fork (this makes sure you have the latest version so there are no conflicts between other users).
│   Go to the content folder: ({user_github_account}/{user_repository_name}/tree/main/src/content).
│   
│       │   Remove your project as shown in the following video.
│   ![Remove Project]({user_remove_project})
│   
│   Contribute by opening up a 'pull request > create pull request'.
│   Now {admin} will get an email notification, as well as having an open pull request that can be approved or disapproved.
│   You now have successfully removed a project. Once {admin} approves of the changes, you can see your project on the official website.
</details>


"""
user_update_project = f""" <details><summary>2. How do I ({user}) update a project?</summary>
│   Please ensure that you are logged in to GitHub.
│   Go to your instance of {admin}'s website located at ({user_github_account}/{user_repository_name}).
│   Sync fork (this makes sure you have the latest version so there are no conflicts between other users).
│   Go to the content folder: ({user_github_account}/{user_repository_name}/tree/main/src/content).
│   
│   Update your project as shown in the following video.
│   ![Update Project]({user_update_project})
│   
│   Contribute by opening up a 'pull request > create pull request'.
│   Now {admin} will get an email notification, as well as having an open pull request that can be approved or disapproved.
│   You now have successfully updated a project. Once {admin} approves of the changes, you can see your project on the official website.
</details>

"""



#demoproject
demoproject_intro = f""" 
### demoproject
In the following section a overview and demo project is provided.You can the coresponding files [here](https://github.com/AnnelotteLammertse/annelottelammertse/example/demoproject)

"""
folder_tree = f""" 
```bash
demo project tree:

├── project_name
│ ├── 1.jpg
│ ├── 2.jpg
│ ├── 3.jpg
│ ├── 4.jpg
│ ├── 5.jpg
│ └── description.txt

```
"""
content_tree = f""" 

```bash
demo `content` folder tree
.
├── {admin}
│   ├── shot_1.jpg
│   └── about_me.txt
├── project_1
│   ├── 1.jpg
│   ├── description
│   └── 2.png
├── project_2
│   ├── 3.jpg 
│   ├── 4.jpg 
│   ├── description.txt
│   ├── 5.png 
│   ├── 6.png 
│   └── 7.jpg 
├── project_3
│   ├── 1.gif
│   ├── 8.jpg
│   ├── 9.png
│   ├── 10.jpg
│   └── description.txt
├── project_4
│   ├── description.txt
│   └── 11.png
├── project_5
│   ├── 11.jpg
│   ├── description.txt
│   └── 12.gif
├── project_6
│   ├── 13.png
│   ├── 14.png
│   ├── 15.jpg
│   ├── 15.jpg
│   ├── 16.jpg
│   └── text.txt
└── project_7
    ├── description.txt
    ├── 17.gif 
    ├── 18.png
    └── 19.jpg 

8 directories, 33 files

```
"""



#demoproject_images
folder_images = f""" 

### images

Images can be of `.jpg`, `.png`, `.gif`, `.HEIC` format.
The max image filezize is 10mb.
the max resolution is 5000x5000 pixels

<div style="display: flex; flex-wrap: wrap;">
    <img src="./example/demoproject/1.jpg" width="32%">
    <img src="./example/demoproject/2.jpg" width="32%">
    <img src="./example/demoproject/3.jpg" width="32%">
    <img src="./example/demoproject/4.jpg" width="32%">
    <img src="./example/demoproject/5.jpg" width="32%">
</div>

"""
folder_description = f""" 
### description
You can only have 1 description. You can upload more but onlt alphabetically first one will be read.
It can have filenames with spaces, and characters.
word, or other office documents or any other word processor is not supported. it can only have a .txt file extension. 

Every `.txt` file in every project should have 4 tags. `<title></title>`, `<date>,</date>`, `<body></body>`, `<tags></tags>`:

They can be used like this:
`<title>the title of your project</title> `
`<date>the date of you project</date>` * this can be in any format you like
`<tags>textile, bioactive, healthcare, wound healing</tags>` *tags (hashtags) are seperated by a comma `,`
`<body>
│       the body text of your project.
│       you cna just write text in here. everytime you start a new line, it will appear on the website. symbols, characters and emoji's are supported
│       
│       optionally, it also supports html styling and tags

│       <h2>subtitle</h2>
│       <details><summary>dropdown menu</summary>
│       │       content of a dropdown menu
│       </details>

│       <p>paragraphs can be used to make different sections</p>

│       <p style='color:red; text-decoration:underline; background-color:blue'>
│       │        You can also style every tag by adding color, underline or inline<span style='background-color:blue;'> background color </span>.
│       </p>
│       
│       <a href="https://duckduckgo.com/">internal or internal links are also supported</a>

│       </body>`

"""
folder_description_example = f""" 
Below is an example of such a `.txt` file

```html
<title>Project 1</title>
<date>10/10/2024</date>
<tags>textile, bioactive, healthcare, wound healing</tags>
<body>
│       <h2>Project Overview</h2>
│       This project focuses on the development of bioactive textiles for applications in wound healing and healthcare. By incorporating bioactive agents into textile fibers, we aim to create functional textiles capable of promoting wound healing, preventing infections, and improving overall healthcare outcomes. The project involves a multidisciplinary approach that combines textile engineering, biomaterials science, and medical research to design innovative solutions for medical textiles.
│       The use of bioactive textiles has the potential to revolutionize wound care by providing continuous, localized delivery of therapeutic agents directly to the wound site. This targeted delivery system minimizes systemic side effects and enhances the efficacy of treatment. Additionally, bioactive textiles offer advantages such as improved patient comfort, reduced dressing changes, and simplified wound management procedures.  

│       The research objectives of the project include investigating methods for functionalizing textile fibers with bioactive agents, optimizing the release kinetics of therapeutic compounds, and evaluating the biocompatibility and safety of bioactive textiles for clinical use. Advanced fabrication techniques such as electrospinning, coating, and grafting will be employed to incorporate bioactive agents into textile matrices while preserving their structural integrity and mechanical properties.

│       <details><summary>Click for more details</summary>This section contains additional details about the project.
│       <a href="https://www.sciencedirect.com/science/article/pii/S014296121830642X">Read this paper</a>
│       <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5799424/">Explore this study</a>
│       <a href="https://www.frontiersin.org/articles/10.3389/fbioe.2020.587592/full">Find out more</a> about advanced fabrication techniques for bioactive textiles.</details>
│       <details><summary>Click for more details</summary>This section contains additional details about the project.</details>

│       <p>The expected outcomes of the project include the development of bioactive textiles with tailored properties for specific medical applications, such as wound dressings, compression garments, and implantable devices. These innovative textiles have the potential to improve patient outcomes, reduce healthcare costs, and advance the field of regenerative medicine.</p>
</body>
```
"""
example_visualized = f""" this demoproject will render out on the website like this:

<div style="display: flex; flex-wrap: wrap;">
    <img src="./example/demoproject/demoproject_text.jpg" width="49%">
    <img src="./example/demoproject/demoproject_web.jpg" width="49%">
</div>
"""




admin_instructions =admin_setup + admin_upload_project + admin_remove_project + admin_update_project + admin_approve_project
user_instructions =user_setup + user_upload_project + user_remove_project + user_update_project 
demoproject =demoproject_intro + content_tree + folder_tree + folder_images + folder_description + folder_description_example + example_visualized

#navigation
navigation_overview = f""" 
## navigation


![{menu_navigation}]({menu_navigation})
![{project_navigation}]({project_navigation})

"""

#workflow
workflow = f""" 
## scripts

every push request activates a github actions protocal  that:
installs:
│       1.imagemagick for image processing
│       
generates:
│       1. the static .html webpages for every project.
│       2. the data.js file that is needed for script.js

uploads:
│       script.js
│       index.html

"""





