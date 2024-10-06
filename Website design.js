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

// Define the schedule
var schedule = [
    {
        start: new Date("July 20, 2024 00:00:01").getTime(),
        end: new Date("July 20, 2024 23:59:59").getTime(),
        message: "Enjoy 50% off on all appetizers today! (Guru Purnima Special)"
    },
    {
        start: new Date("July 21, 2024 00:00:00").getTime(),
        end: new Date("July 21, 2024 23:59:59").getTime(),
        message: "Get a free drink with every meal this Sunday!"
    },
    {
        start: new Date("July 22, 2024 00:00:00").getTime(),
        end: new Date("July 22, 2024 23:59:59").getTime(),
        message: "Every dish you eat from bundle 20% off on dessert."
    }
];

// Function to check if current time is within any of the scheduled periods
function getCurrentSchedule() {
    var now = new Date().getTime();
    for (var i = 0; i < schedule.length; i++) {
        if (now >= schedule[i].start && now <= schedule[i].end) {
            return schedule[i];
        }
    }
    return null;
}

// Display the popup if within the schedule
var currentSchedule = getCurrentSchedule();
if (currentSchedule) {
    setTimeout(function() {
        popupMessage.textContent = currentSchedule.message;
        popup.style.display = "block";
    }, 2000); // Delay before showing the popup
} else {
    // If not within schedule, show new message
    setTimeout(function() {
        popupMessage.textContent = "For booking in the weekdays, 20% off";
        popup.style.display = "block";
    }, 2000); // Delay before showing the popup
}
