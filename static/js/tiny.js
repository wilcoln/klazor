function openTinyFolderContextMenu(e, id) {
    let contextmenuId = "fmenu_" + id
    openContextMenu(e, contextmenuId)
}

function openTinySheetContextMenu(e, id) {
    let contextmenuId = "smenu_" + id
    openContextMenu(e, contextmenuId)
}
function openTinyCourseContextMenu(e, id) {
    let contextmenuId = "cmenu_" + id
    openContextMenu(e, contextmenuId)
}

function openTinyFileContextMenu(e, id) {
    let contextmenuId = "file-menu_" + id
    openContextMenu(e, contextmenuId)
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