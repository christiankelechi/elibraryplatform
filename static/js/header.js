


// HEADER SCRIPT
const toggleBar =  document.querySelector(".toggle-bar");
const  closeToggleBar=  document.querySelector(".close-toggle-bar");
const navMenu =  document.querySelector(".nav-menu");

toggleBar.addEventListener("click",function(e){
navMenu.classList.add("active")
});

// Close the toggle menu
closeToggleBar.addEventListener("click",function(e){
navMenu.classList.toggle("active");
})