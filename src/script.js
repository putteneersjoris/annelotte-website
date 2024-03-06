var PIXELDISTANCE = 4


var projectsData = content.projects;

var barData = "";
// var allTagsDataArray = content.allTags
var barArray = content.barContent;
for (var i = 0; i < barArray.length; i++) {
  barData += barArray[i];
}
document.getElementById('barContent').innerHTML = barData


// set tags
var allTagsData = "";
var allTagsDataArray =  content.allTags
for (var i = 0; i < allTagsDataArray.length; i++) {
    allTagsData += allTagsDataArray[i];
}

// Get the tags-wrapper element and set its innerHTML


document.getElementById('tags-wrapper').innerHTML = "<span id='all' style='text-decoration:underline;'>#all<br><br><br></span>"  +  allTagsData;

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
      
	var imgATag = document.createElement("a");
	imgATag.href = projectName + ".html"
	var imgTag = document.createElement("img");
	imgTag.src = project.images[0];

	imgATag.appendChild(imgTag)          
	spanTag.appendChild(imgATag);

      
	// Create an <a> tag with project.html as href
	var aTag = document.createElement("a");
	aTag.href = projectName + ".html";
	var divEndImg = document.createElement("div");
	divEndImg.classList.add("endImg");
	// aTag.style

	var divProjectName = document.createElement("div");
	divProjectName.classList.add("projectName");
	divProjectName.textContent = projectName;


	var divProjectDate = document.createElement("div");
	divProjectDate.classList.add("projectDate");
	divProjectDate.textContent = project.date;

	// Create the <div> element with class "projectTags"
	var divProjectTags = document.createElement("div");
	divProjectTags.classList.add("projectTags");
	divProjectTags.innerHTML = project.tags

	divEndImg.appendChild(divProjectName);
	divEndImg.appendChild(divProjectDate);
	divEndImg.appendChild(divProjectTags);
	aTag.appendChild(divEndImg);

	spanTag.appendChild(aTag);

	var projectsTag = document.getElementById("projects")

	projectsTag.appendChild(spanTag);
	}
}


// Get the div with id "projects"
const projectsDiv = document.getElementById("projects");

// Define a function to update the width of the elements based on the div's width
function updateWidth() {
    // Get the current width of the div
    const width = projectsDiv.offsetWidth;
   console.log(width) 
    // Calculate the width for each "project" class
    const n_projects = 5;
    const dist = (Math.floor(width / n_projects) - 3) + "px";
    
    // Set the width for each "project" class
    const projectElements = document.getElementsByClassName('project');
    for (let i = 0; i < projectElements.length; i++) {
        let imgTags = projectElements[i].getElementsByTagName('img');
        for (let j = 0; j < imgTags.length; j++) {
            imgTags[j].style.width = dist;
            imgTags[j].style.height = dist;
        }
    }
    
    // Set the width for each element with class "endImg"
    const projectElementsImg = document.getElementsByClassName('endImg');
    for (let i = 0; i < projectElementsImg.length; i++) {
        projectElementsImg[i].style.width = dist;
        projectElementsImg[i].style.height = dist;
    }
}

// Call updateWidth initially to set the initial width
updateWidth();

// Add a resize event listener to the window object to call updateWidth whenever the window is resized
window.addEventListener('resize', updateWidth);


// set date on footer
var currentDate = new Date
var year = currentDate.getFullYear()
document.getElementById('footerTextRight').innerHTML = "@" + year


const filters = document.querySelectorAll('.filter');
const projects = document.querySelectorAll('.project');
const all = document.getElementById('all');
let selectedFilters = [];

all.addEventListener("click", function() {
    var styleAttr = all.getAttribute("style");

    if (!styleAttr || styleAttr.indexOf('text-decoration: none') === -1) {
        all.style.textDecoration = "none";
        console.log("Set all projects to hidden");
        projects.forEach(project => {
            project.classList.add('hidden');
        });
    } else {
        all.style.textDecoration = "underline";
        console.log("Revealing all projects");
        projects.forEach(project => {
            project.classList.remove('hidden');
        });
        filters.forEach(filter => {
            filter.classList.remove('selected');
        });
    }
});

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

        // Check if "all" is selected
        const allSelected = selectedFilters.includes('all');

        projects.forEach(project => {
            const tags = project.getAttribute('data-tags');
            if (allSelected || selectedFilters.every(tag => tags.includes(tag))) {
                project.classList.remove('hidden');
            } else {
                project.classList.add('hidden');
            }
        });

        // Check if no filters are selected and display message
        if (selectedFilters.length === 0) {
            all.style.textDecoration = "underline";
        } else {
            all.style.textDecoration = "none";
        }
    });
});


