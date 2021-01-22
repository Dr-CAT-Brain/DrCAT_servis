"use strict";

let fileInput = document.getElementById("id_photo");
let dropContainer = document.getElementById("input-container");
let img = document.getElementById("avatar-img");

fileInput.addEventListener("change", function (e) {
  dropContainer.innerHTML = fileInput.files[0].name;

  img.file = fileInput.files[0];

  var reader = new FileReader();
  reader.onload = (function(aImg) { return function(e) { aImg.src = e.target.result; }; })(img);
  reader.readAsDataURL(fileInput.files[0]);
});

let name1 = document.getElementById("id_full_name");
let email = document.getElementById("id_email");
let password = document.getElementById("id_password1");
let password2 = document.getElementById("id_password2");

let eventElems = [name1, email, password, password2]

let sendButton = document.getElementById("send");

const SetButtonActiveEvent = () => {
    if (name1.value != "" && email.value != "" && password.value != "" && password2.value != "") {
        sendButton.style.backgroundColor = "#004dc1";
        sendButton.style.color = "#ffffff";
        $(sendButton).attr("disabled", false);
    } else {
        sendButton.style.backgroundColor = "#ffffff";
        sendButton.style.color = "#aaaaaa";
        $(sendButton).attr("disabled", true);
    }
}

for (let i=0; i < eventElems.length; i++){
    eventElems[i].addEventListener("input", (event) => {
        SetButtonActiveEvent();
    });
}
