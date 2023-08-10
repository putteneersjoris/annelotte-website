var projectsData = content.projects;
// var allTagsData = content.allTags;
// var barData = content.barContent;

// set bar


var barData = "";
// var allTagsDataArray = content.allTags
var barArray = content.barContent;
for (var i = 0; i < barArray.length; i++) {
  barData += barArray[i];
}
document.getElementById('barContent').innerHTML = barData




// set tags
var allTagsData = "";
var allTagsDataArray = content.allTags
for (var i = 0; i < allTagsDataArray.length; i++) {
    allTagsData += allTagsDataArray[i];
}

// Get the tags-wrapper element and set its innerHTML
document.getElementById('tags-wrapper').innerHTML = allTagsData;

// Loop over each project in the "projects" object
for (var projectName in content.projects) {
  if (content.projects.hasOwnProperty(projectName)) {
      var project = content.projects[projectName];
  }
}

var nProjects = 0
for (var projectName in content.projects) {
  if (content.projects.hasOwnProperty(projectName)) {
      var project = content.projects[projectName];
      nProjects +=1
      // Create a <span> tag
      var spanTag = document.createElement("span");
      spanTag.classList.add("project")
      spanTag.style.zIndex = 100-nProjects
      spanTag.setAttribute("data-tags", project.tags.join(" "));
      // spanTag.style.zIndex = 99 - index;
      
      // add start image
      var startImg = document.createElement("img");
      startImg.classList.add('startImg')
      // startImg.style.zIndex = 
      startImg.src = "/src/extra/end.png"
      // Loop over images and create <img> tags
      
      spanTag.appendChild(startImg);
      var nImg = -1
      project.images.forEach(function(imageSrc, index) {
          var imgTag = document.createElement("img");
          imgTag.src = imageSrc;
          imgTag.style.top = `${index * 3}px`
          imgTag.style.left = `${index * 3}px`

          nImg +=1
          
          spanTag.appendChild(imgTag);
      });


      
      // Create an <a> tag with project.html as href
      var aTag = document.createElement("a");
      aTag.href = projectName + ".html";
      var divEndImg = document.createElement("div");
      divEndImg.classList.add("endImg");
      // aTag.style
      
      var divProjectName = document.createElement("div");
      divProjectName.classList.add("projectName");
      divProjectName.textContent = projectName;
      divProjectName.style.top = `${nImg * 3}px`;
      divProjectName.style.left = `${nImg * 3}px`;


      var divProjectDate = document.createElement("div");
      divProjectDate.classList.add("projectDate");
      divProjectDate.textContent = project.date;
      divProjectDate.style.bottom = `-${nImg * 3}px`;
      divProjectDate.style.right = `-${30 + nImg * 3}px`;
      console.log(project.date);

      // Create the <div> element with class "projectTags"
      var divProjectTags = document.createElement("div");
      divProjectTags.classList.add("projectTags");
      divProjectTags.innerHTML = project.tags
      divProjectTags.style.bottom = `-${nImg * 3}px`;
      divProjectTags.style.left = `${30 + nImg * 3}px`;

      divEndImg.appendChild(divProjectName);
      divEndImg.appendChild(divProjectDate);
      divEndImg.appendChild(divProjectTags);
      aTag.appendChild(divEndImg);


      // Append <a> tag to <span> tag
      // spanTag.style.border = "10px solid red"
      spanTag.appendChild(aTag);
      
      document.getElementById("projects").appendChild(spanTag);
  }
}




// set date on footer
var currentDate = new Date
var year = currentDate.getFullYear()
document.getElementById('footerTextRight').innerHTML = "@" + year


// make filter system
const filters = document.querySelectorAll('.filter');
        const projects = document.querySelectorAll('.project');
        const selectedFilters = [];

        filters.forEach(filter => {
          filter.addEventListener('click', () => {
            const filterValue = filter.getAttribute('data-filter');
            const isSelected = selectedFilters.includes(filterValue);
            
            // Toggle the selected state
            if (isSelected) {
              const index = selectedFilters.indexOf(filterValue);
              selectedFilters.splice(index, 1);
              filter.classList.remove('selected');
            } else {
              selectedFilters.push(filterValue);
              filter.classList.add('selected');
            }

            projects.forEach(project => {
              const tags = project.getAttribute('data-tags');
              if (selectedFilters.every(tag => tags.includes(tag))) {
                project.classList.remove('hidden');
              } else {
                project.classList.add('hidden');
              }
            });
          });
        });




// in pages make images big when clicked

function toggleSize(image) {
  if (image.style.width === '98.5%') {
      image.style.width = '32.5%';
  } else {
      image.style.width = '98.5%';
      // image.style.height = '50%';
  }
}


