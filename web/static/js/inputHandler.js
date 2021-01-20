"use strict";
//#region screen1
let frame = document.getElementById("frame");

function radioHandler1(target) {
    switch (target) {
        case document.getElementById("deficit-1l"):
            frame.style.left = "0";
            frame.style.borderTopLeftRadius = "20px";
            frame.style.borderBottomLeftRadius = "20px";

            frame.style.maxWidth = "293px";

            frame.style.borderTopRightRadius = "0";
            frame.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("deficit-2l"):
            frame.style.left = "293px";
            frame.style.borderTopLeftRadius = "0";
            frame.style.borderBottomLeftRadius = "0";

            frame.style.maxWidth = "293px";

            frame.style.borderTopRightRadius = "0";
            frame.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("deficit-3l"):
            frame.style.left = "585px";
            frame.style.borderTopLeftRadius = "0";
            frame.style.borderBottomLeftRadius = "0";

            frame.style.maxWidth = "293px";

            frame.style.borderTopRightRadius = "0";
            frame.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("deficit-4l"):
            frame.style.left = "879px";
            frame.style.borderTopLeftRadius = "0";
            frame.style.borderBottomLeftRadius = "0";

            frame.style.maxWidth = "319px";

            frame.style.borderTopRightRadius = "20px";
            frame.style.borderBottomRightRadius = "20px";
            break;
    }
}

let frame2 = document.getElementById("frame2");

function radioHandler2(target) {
    switch (target) {
        case document.getElementById("level-1l"):
            frame2.style.left = "0";
            frame2.style.borderTopLeftRadius = "20px";
            frame2.style.borderBottomLeftRadius = "20px";

            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-2l"):
            frame2.style.left = "171px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";


            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-3l"):
            frame2.style.left = "342px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";

            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-4l"):
            frame2.style.left = "513px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";

            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-5l"):
            frame2.style.left = "684px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";

            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-6l"):
            frame2.style.left = "856px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";

            frame2.style.borderTopRightRadius = "0";
            frame2.style.borderBottomRightRadius = "0";
            break;
        case document.getElementById("level-7l"):
            frame2.style.left = "1026px";
            frame2.style.borderTopLeftRadius = "0";
            frame2.style.borderBottomLeftRadius = "0";

            frame2.style.borderTopRightRadius = "20px";
            frame2.style.borderBottomRightRadius = "20px";
            break;
    }
}
//#endregion

let disabledNow1 = false;
let disabledNow2 = false;

//#region screen2
function checkboxHandler1(target) {
    disabledNow1 = !disabledNow1;
    let checkBoxs = document.querySelectorAll("#pathology > .row > .col-auto > input");
    let pS = document.querySelectorAll("#pathology > .row > .col-auto > p");

    let checkboxUnknown = document.querySelector("#checkboxUnknown1");
    let checkboxNone = document.querySelector("#checkboxNone1");

    checkBoxs.forEach(element => {
        $(element).attr("disabled", disabledNow1);
    });

    switch(target) {
        case checkboxUnknown:
            $(checkboxNone).attr("disabled", disabledNow1);
        break;
        case checkboxNone:
            $(checkboxUnknown).attr("disabled", disabledNow1);
        break;
    }

    pS.forEach(element => {
        if (disabledNow1) {
            element.style.color = "#aaaaaa";
        } else {
            element.style.color = "black";
        }
    });
}

function checkboxHandler2(target) {
    disabledNow2 = !disabledNow2;
    let checkBoxs = document.querySelectorAll("#other > .row > .col-auto > input");
    let pS = document.querySelectorAll("#other > .row > .col-auto > p");

    let checkboxUnknown = document.querySelector("#checkboxUnknown2");
    let checkboxNone = document.querySelector("#checkboxNone2");

    checkBoxs.forEach(element => {
        $(element).attr("disabled", disabledNow2);
    });

    switch(target) {
        case checkboxUnknown:
            $(checkboxNone).attr("disabled", disabledNow2);
        break;
        case checkboxNone:
            $(checkboxUnknown).attr("disabled", disabledNow2);
        break;
    }

    pS.forEach(element => {
        if (disabledNow2) {
            element.style.color = "#aaaaaa";
        } else {
            element.style.color = "black";
        }
    });
}

//блокировка кнопки "Далее1"
let checkedBoxs1 = $("#mainPathology > [type='checkbox']:checked").length;
let checkBoxs2 = $("#mainOther > [type='checkbox']:checked").length;

$('#mainPathology :checkbox').change(function () {
    if (this.checked) {
        checkedBoxs1 += 1;

        if (checkedBoxs1 != 0 && checkBoxs2 != 0) {
            document.getElementById("btnNext1").style.backgroundColor = "#004dc1";
            document.querySelector("#btnNext1 > div").style.backgroundColor = "#004dc1";
            document.querySelector("#btnNext1 > div > p").style.color = "white";
            document.querySelector("#btnNext1 > div").style.cursor = "pointer";
            $(document.querySelector("#btnNext1 > div")).attr("onclick", "nextScreen2()");
        }
    } else {
        checkedBoxs1 -= 1;

        if (checkedBoxs1 == 0 || checkBoxs2 == 0) {
            document.getElementById("btnNext1").style.backgroundColor = "#ffffff";
            document.querySelector("#btnNext1 > div").style.backgroundColor = "#ffffff";
            document.querySelector("#btnNext1 > div > p").style.color = "#aaaaaa";
            document.querySelector("#btnNext1 > div").style.cursor = "default";
            $(document.querySelector("#btnNext1 > div")).attr("onclick", "");
        }
    }
});

$('#mainOther :checkbox').change(function () {
    if (this.checked) {
        checkBoxs2 += 1;

        if (checkedBoxs1 != 0 && checkBoxs2 != 0) {
            document.getElementById("btnNext1").style.backgroundColor = "#004dc1";
            document.querySelector("#btnNext1 > div").style.backgroundColor = "#004dc1";
            document.querySelector("#btnNext1 > div > p").style.color = "white";
            document.querySelector("#btnNext1 > div").style.cursor = "pointer";
            $(document.querySelector("#btnNext1 > div")).attr("onclick", "nextScreen2()");
        }
    } else {
        checkBoxs2 -= 1;

        if (checkedBoxs1 == 0 || checkBoxs2 == 0) {
            document.getElementById("btnNext1").style.backgroundColor = "#ffffff";
            document.querySelector("#btnNext1 > div").style.backgroundColor = "#ffffff";
            document.querySelector("#btnNext1 > div > p").style.color = "#aaaaaa";
            document.querySelector("#btnNext1 > div").style.cursor = "default";
            $(document.querySelector("#btnNext1 > div")).attr("onclick", "");
        }
    }
});

//#endregion


document.getElementById("id_snapshot").addEventListener("change", function(e) {
    fileUploaded();
});

//grad & drop
let fileInput = document.getElementById("id_snapshot");
let dropContainer = document.getElementById("select");

dropContainer.ondragover = dropContainer.ondragenter = function(evt) {
    evt.preventDefault();
  };
  
  dropContainer.ondrop = function(evt) {
    fileInput.files = evt.dataTransfer.files;
    fileUploaded();
    evt.preventDefault();
};

function fileUploaded() {
    dropContainer.style.opacity = "0";
    dropContainer.style.visibility = "hidden";
    dropContainer.style.display = "none";
    
    document.querySelector("#file-list").style.display = "block";
    document.querySelector("#file-list").style.visibility = "visible";
    document.querySelector("#file-list").style.opacity = "1";

    let fileText = document.querySelector("#file-list > .file > .col-auto > p");
    fileText.innerHTML = fileInput.files[0].name;

    let btnMainDiv = document.querySelector("#btnNext3");
    let btnDiv = document.querySelector("#btnNext3 > label");
    let btnText = document.querySelector("#btnNext3 > label > p");

    btnMainDiv.style.backgroundColor = "#ff2828";
    btnDiv.style.backgroundColor = "#ff2828";
    btnText.style.color = "white";
    btnText.style.cursor = "pointer";
    btnDiv.style.cursor = "pointer";
}

function preventDefaultInput(target) {
    target.value = "";

    document.querySelector("#file-list").style.opacity = "0";
    document.querySelector("#file-list").style.visibility = "hidden";
    document.querySelector("#file-list").style.display = "none";
    
    dropContainer.style.display = "flex";
    dropContainer.style.visibility = "visible";
    dropContainer.style.opacity = "1";

    let btnMainDiv = document.querySelector("#btnNext3");
    let btnDiv = document.querySelector("#btnNext3 > label");
    let btnText = document.querySelector("#btnNext3 > label > p");

    btnMainDiv.style.backgroundColor = "#ffffff";
    btnDiv.style.backgroundColor = "#ffffff";
    btnText.style.color = "#aaaaaa";
    btnText.style.cursor = "default";
    btnDiv.style.cursor = "default";
}