let HideEditMenu = () => {
    $("#id_edit_div").fadeOut();
};

let ShowEditMenu = () => {
    $("#id_edit_div").show("slow");
};

let HideProfileInfo = () => {
    $("#id_personal_info").hide();
};

let ShowProfileInfo = () => {
    $("#id_personal_info").show("slow");
};


$(document).ready(function () {
    $('#id_editing_start').click(() => {
        HideProfileInfo();
        ShowEditMenu();
    });

    $('#id_cancel_editing').click(function() {
        HideEditMenu();
        ShowProfileInfo();
    });

    HideEditMenu();
});
