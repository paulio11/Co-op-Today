//assigning container and sidebar to variables.
let sidebarContainer = document.getElementById('sidebar-container');
let sidebarMenu = document.getElementById('sidebar');

//close sidebar if clicked outside of it.
sidebarContainer.addEventListener('click', closeSidebar);

//add event listener to menu button -> run openSidebar.
let menuButton = document.getElementById('menu-button');
menuButton.addEventListener('click', openSidebar);

//add event listener to close button -> run closeSidebar.
let closeMenu = document.getElementById('close-menu');
closeMenu.addEventListener('click', closeSidebar);

/**
 * Make container visible, disable scrolling, open sidebar.
 */
function openSidebar() {

    sidebarContainer.style.visibility = 'visible';
    document.body.style.overflow = 'hidden';
    sidebarMenu.classList.remove('sidebar-closed');
    sidebarMenu.classList.add('sidebar-open');

}

/**
 * Make container invisible, enable scrolling, close sidebar.
 */
function closeSidebar() {

    sidebarContainer.style.visibility = 'hidden';
    document.body.style.overflow = 'initial';
    sidebarMenu.classList.remove('sidebar-open');
    sidebarMenu.classList.add('sidebar-closed');

}