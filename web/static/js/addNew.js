"use strict";

setTimeout(() => document.getElementById("progress-bar").style.width = window.innerWidth * 0.8 / 3  + "px", 500);

function nextScreen1() {
    document.getElementById("screen1").style.visibility = "hidden";
    document.getElementById("screen1").style.opacity = "0"; //закрываем screen1
    document.getElementById("screen1").style.display = "none";

    document.getElementById("screen2").style.display = "block";
    document.getElementById("screen2").style.visibility = "visible";
    document.getElementById("screen2").style.opacity = "1"; //открываем screen2

    document.getElementById("progress-bar").style.width = window.innerWidth * 0.8 / 3 * 2  + "px";

    document.getElementById("title").innerHTML = "Анамез";
}

function previousScreen1() {
    document.getElementById("screen2").style.opacity = "0"; //закрываем screen2
    document.getElementById("screen2").style.visibility = "hidden";
    document.getElementById("screen2").style.display = "none";

    document.getElementById("screen1").style.display = "block";
    document.getElementById("screen1").style.visibility = "visible";
    document.getElementById("screen1").style.opacity = "1"; //открываем screen1

    document.getElementById("progress-bar").style.width = window.innerWidth * 0.8 / 3  + "px";

    document.getElementById("title").innerHTML = "Данные о пациенте";
}


function nextScreen2() {
    document.getElementById("screen2").style.opacity = "0"; //закрываем screen2
    document.getElementById("screen2").style.visibility = "hidden";
    document.getElementById("screen2").style.display = "none";

    document.getElementById("screen3").style.display = "block";
    document.getElementById("screen3").style.visibility = "visible";
    document.getElementById("screen3").style.opacity = "1"; //открываем screen1

    document.getElementById("progress-bar").style.borderTopRightRadius = "10px";
    document.getElementById("progress-bar").style.borderBottomRightRadius = "10px";
    document.getElementById("progress-bar").style.width = window.innerWidth * 0.8051 + "px";

    document.getElementById("title").innerHTML = "Загрузка снимка";
}

function previousScreen3() {
    document.getElementById("screen3").style.opacity = "0"; //закрываем screen2
    document.getElementById("screen3").style.visibility = "hidden";
    document.getElementById("screen3").style.display = "none";

    document.getElementById("screen2").style.display = "block";
    document.getElementById("screen2").style.visibility = "visible";
    document.getElementById("screen2").style.opacity = "1"; //открываем screen1

    document.getElementById("progress-bar").style.width = window.innerWidth * 0.8 / 3 * 2  + "px";

    document.getElementById("title").innerHTML = "Анамез";
}