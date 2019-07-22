// Navbr and toolbar animation
onscroll = function () {
    let sheetToolbar = $(".sheet-toolbar");
    let modificationInfo = $("#info-modification");
    if (scrollY > 40) {
        sheetToolbar.css('background', 'white')
    } else {
        sheetToolbar.css('background', 'transparent')
    }
}