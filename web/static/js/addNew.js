"use strict";

setTimeout(() => document.getElementById("progress-bar").style.width = window.innerWidth / 3 + "px", 500);

let secondEl = document.createElement("form");
secondEl.innerHTML = "<h2>Загрузите КТ снимок</h2><input type='file' id='fileInput'><label for='fileInput'><img src='assets/img/upload.png' alt='Нажмите сюда'></label>";

function secondStep() {
    let form = document.getElementById("form");
    let title = document.getElementById("title");

    title.innerHTML = "2. Загрузите КТ снимок";
    form.parentNode.replaceChild(secondEl, form);
}