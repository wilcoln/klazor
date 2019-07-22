document.onclick = closeAllContextMenu // Close all context menu on click
function closeAllContextMenu(){
    let contextmenus = document.querySelectorAll('.rmenu');
    for(let contextmenu of contextmenus)
        contextmenu.className = "rmenu hide"
}
function openContextMenu(e, contextMenuId){
    e.preventDefault()
    closeAllContextMenu()
    document.getElementById(contextMenuId).className = "rmenu show";
    document.getElementById(contextMenuId).style.top = e.clientY + 'px';
    document.getElementById(contextMenuId).style.left = e.clientX + 'px';
}

function openFolderContextMenu(e, id) {
    let contextMenuId = "folder-menu_" + id
    openContextMenu(e, contextMenuId)
}