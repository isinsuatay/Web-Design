//-----------------Signin/Login ------------------

document.addEventListener('DOMContentLoaded', function () {
  const loginBtn = document.getElementById('loginBtn');
  const loginPopup = document.getElementById('loginPopup');
  const loginCloseBtn = document.getElementById('loginCloseBtn');
  const loginForm = document.getElementById('loginForm');

  const registerBtn = document.getElementById('registerBtn');
  const registerPopup = document.getElementById('registerPopup');
  const registerCloseBtn = document.getElementById('registerCloseBtn');
  const registerForm = document.getElementById('registerForm');

  const logoutBtn = document.getElementById('logoutBtn');

  hideLogoutBtn();

  loginBtn.addEventListener('click', function () {
    loginPopup.style.display = 'block';
  });

  loginCloseBtn.addEventListener('click', function () {
    loginPopup.style.display = 'none';
  });


  loginForm.addEventListener('submit', function (a) {
    a.preventDefault();
    const passwordInput = loginForm.querySelector('input[type="password"]');
    if (passwordInput.value.length < 8) {
      alert('Your password must be at least 8 characters long.');
      return;
    }
    alert('Login successful.');
    loginPopup.style.display = 'none';
    showLogoutBtn();
  });

  registerBtn.addEventListener('click', function () {
    registerPopup.style.display = 'block';
  });

  registerCloseBtn.addEventListener('click', function () {
    registerPopup.style.display = 'none';
  });

  registerForm.addEventListener('submit', function (a) {
    a.preventDefault();
    const passwordInput = registerForm.querySelector('input[type="password"]');
    if (passwordInput.value.length < 8) {
      alert('Your password must be at least 8 characters long.');
      return;
    }
    alert('Your account has been successfully created!');
    registerPopup.style.display = 'none';
    showLogoutBtn();
  });

  logoutBtn.addEventListener('click', function () {
    hideLogoutBtn();
  });

  function showLogoutBtn() {
    loginBtn.style.display = 'none';
    registerBtn.style.display = 'none';
    logoutBtn.style.display = 'inline-block';
  }

  function hideLogoutBtn() {
    logoutBtn.style.display = 'none';
    loginBtn.style.display = 'inline-block';
    registerBtn.style.display = 'inline-block';
  }
});

// ----------------Dropdown--------------------

let dropdownBtn = document.querySelector(".dropdown-btn");
let dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", function() {
  if (dropdownContent.style.display === "none") {
    dropdownContent.style.display = "block";
  } else {
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
document.getElementById("bolum1").style.display = "block";
document.getElementById("bolum2").style.display = "none";
document.getElementById("bolum3").style.display = "none";


setTimeout(function () {
  document.getElementById("bolum1").style.display = "none";
  document.getElementById("bolum2").style.display = "none";
  document.getElementById("bolum3").style.display = "block";


  setInterval(function () {
    let bolum1 = document.getElementById("bolum1");
    let bolum2 = document.getElementById("bolum2");
    let bolum3 = document.getElementById("bolum3");

    if (bolum1.style.display === "none" && bolum2.style.display === "none") {
      bolum1.style.display = "block";
      bolum2.style.display = "none";
      bolum3.style.display = "none";
    }
    else if (bolum1.style.display === "block") {
      bolum1.style.display = "none";
      bolum2.style.display = "block";
      bolum3.style.display = "none";
    }
    else {
      bolum1.style.display = "none";
      bolum2.style.display = "none";
      bolum3.style.display = "block";
    }

  }, 3000);
}, 3000);

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



