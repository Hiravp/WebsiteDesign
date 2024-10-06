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
