
// Password_Script
const formEl  = document.querySelector(".form-container form");
const passwordEls = document.querySelectorAll(`input[type='password']`);
const eyeIcon = document.querySelectorAll(".eye-icon");
console.log(eyeIcon)

const showPassword = password => !password;
let passwordState = false;

const handleTogglePasswod = (e) => {
passwordState = !passwordState;

if(!e.target.classList.contains("password") && !e.target.classList.contains("eye-icon")){
return;
}
if(e.target.classList.contains("eye-icon")){
passwordEls.forEach((item,index) => passwordState ? item.type = "text" : item.type = "password")
}
}

// add an event listener
formEl.addEventListener('click',handleTogglePasswod);