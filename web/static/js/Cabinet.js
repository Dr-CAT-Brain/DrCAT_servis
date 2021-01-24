let HideEditMenu = () => {
    $("#id_edit_form").fadeOut();
};

let ShowEditMenu = () => {
    $("#id_edit_form").show("slow");
};

let HideProfileInfo = () => {
    $("#id_personal_info").fadeOut();
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
