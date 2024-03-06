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

```py

print(os)


```



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























