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


var projectsData = content.projects;
var allTagsData = content.allTags;
var barData = content.bar;

console.log("Projects:", projectsData);
console.log("All Tags:", allTagsData);
console.log("Bar:", barData);