
// ----------------Dropdown--------------------
let dropdownBtn = document.querySelector(".dropdown-btn");
let dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", function(event) {
  dropdownContent.style.display = "block";
  event.stopPropagation();
});

document.addEventListener("click", function(event) {
  if (!event.target.closest('.dropdown')) {
    dropdownContent.style.display = "none";
  }
});

// SideNav 
function openNav() {
  document.getElementById("YanMenu").style.width = "250px";
}

function closeNav() {
  document.getElementById("YanMenu").style.width = "0";
}

//--------- HERO IMAGE ---------
document.addEventListener("DOMContentLoaded", function () {
  const part1 = document.getElementById("part1");
  const part2 = document.getElementById("part2");
  const part3 = document.getElementById("part3");

  part1.style.display = "block";
  part2.style.display = "none";
  part3.style.display = "none";

  setTimeout(function () {
      part1.style.display = "none";
      part2.style.display = "none";
      part3.style.display = "block";

      setInterval(function () {
          if (part1.style.display === "none" && part2.style.display === "none") {
              part1.style.display = "block";
              part2.style.display = "none";
              part3.style.display = "none";
          } else if (part1.style.display === "block") {
              part1.style.display = "none";
              part2.style.display = "block";
              part3.style.display = "none";
          } else {
              part1.style.display = "none";
              part2.style.display = "none";
              part3.style.display = "block";
          }
      }, 3000);
  }, 3000);
});


// -----------Slider------------

new Glide('.glide', {
    type: 'carousel', 
    startAt: 0, 
    perView: 3, 
    focusAt: 'center', 
    gap: 50, 
    breakpoints: {
        576: {
            perView: 1 
        }
    }
}).mount();

// --------------FOOTER----------------

const emailInput = document.getElementById("email");
const checkboxContainer = document.getElementById("checkboxContainer");
const checkbox = document.getElementById("checkbox");

emailInput.addEventListener("input", function () {
  const emailValue = emailInput.value;

  if (validateEmail(emailValue)) {
    checkboxContainer.style.display = "block";
  } else {
    checkboxContainer.style.display = "none";
    checkbox.checked = false;
  }
});

function validateEmail(email) {
  const emailRegex = /\S+@\S+\.\S+/;
  return emailRegex.test(email);
}

// ----- SEPET ------
