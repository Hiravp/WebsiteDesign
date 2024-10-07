function toggleMenu(id) {
    let menu = document.getElementById(id);
    let menus = document.querySelectorAll('.dropdown-menu');

    menus.forEach((m) => {
        if (m !== menu) {
            m.style.display = 'none';
        }
    });

    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}








window.addEventListener('scroll', reveal);

function reveal() {
    var reveals = document.querySelectorAll('.reveal');

    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var revealTop = reveals[i].getBoundingClientRect().top;
        var revealPoint = 150;

        if (revealTop < windowHeight - revealPoint) {
            reveals[i].classList.add('active');
        } else {
            reveals[i].classList.remove('active');
        }
    }
}



// script.js

// Get the popup
var popup = document.getElementById("dealPopup");

// Get the <span> element that closes the popup
var span = document.getElementsByClassName("close")[0];
const popupMessage = document.getElementById("popup-message");

// When the user clicks on <span> (x), close the popup
span.onclick = function() {
    popup.style.display = "none";
}

// When the user clicks anywhere outside of the popup, close it
window.onclick = function(event) {
    if (event.target == popup) {
        popup.style.display = "none";
    }
}
