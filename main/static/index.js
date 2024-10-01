// script.js




const navbarMenu = document.querySelector(".navbar .links");


const showPopupBtn = document.querySelector(".Login-btn");
const formPopup = document.querySelector(".form-popup ");
const hidePopupBtn = document.querySelector(".form-popup .close-btn");
const loginSignupLink = document.querySelectorAll(".form-box .button-link a");


//showpopup//
showPopupBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-popup");
});
//hidepopup//
hidePopupBtn.addEventListener("click", () => showPopupBtn.click());


loginSignupLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        formPopup.classList[link.id === "signup-link" ? 'add' : 'remove']("show-signup");

    });
    
});


            