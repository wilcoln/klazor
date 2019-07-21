document.onclick = closeAllContextMenu // Close all context menu on click

function closeAllContextMenu(){
    let contextmenus = document.querySelectorAll('.rmenu');
    for(let contextmenu of contextmenus)
        contextmenu.className = "rmenu hide"
}
function openTinyFolderContextMenu(e, id) {
    let contextmenuId = "fmenu_" + id
    openTinyContextMenu(e, contextmenuId)
}

function openTinySheetContextMenu(e, id) {
    let contextmenuId = "smenu_" + id
    openTinyContextMenu(e, contextmenuId)
}
function openTinyCourseContextMenu(e, id) {
    let contextmenuId = "cmenu_" + id
    openTinyContextMenu(e, contextmenuId)
}

function openTinyFileContextMenu(e, id) {
    let contextmenuId = "file-menu_" + id
    openTinyContextMenu(e, contextmenuId)
}
function openTinyContextMenu(e, contextMenuId){
    e.preventDefault()
    closeAllContextMenu()
    document.getElementById(contextMenuId).className = "rmenu show";
    document.getElementById(contextMenuId).style.top = e.clientY*.001 + 'px';
    document.getElementById(contextMenuId).style.left = e.clientX*.25 + 'px';
    window.event.returnValue = false;
}
function deleteFolder(id) {
    axios({
        method: 'post',
        url: '/folder/delete/' + id + '/',
        headers: {
            "X-CSRFToken": Cookies.get('csrftoken'),
        }
    }).then((response) => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    });
}

function deleteSheet(id) {
    axios({
        method: 'post',
        url: '/sheet/delete/' + id + '/',
        headers: {
            "X-CSRFToken": Cookies.get('csrftoken'),
        }
    }).then((response) => {
        console.log(response)
    }).catch((error) => {
        console.log(error)
    });
}