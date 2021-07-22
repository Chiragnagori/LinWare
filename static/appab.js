const hamburger_menu = document.querySelector(".hamburger-menu");
const container = document.querySelector(".container");

hamburger_menu.addEventListener("click", () => {
  container.classList.toggle("active");
});

function myFunction() {
  
  document.getElementById("demo").innerHTML = location.href= "about.html"; 
    
}

function getintouch(){
  document.getElementById("demo").innerHTML = location.href = "/navi_team";
}