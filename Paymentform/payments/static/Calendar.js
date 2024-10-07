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