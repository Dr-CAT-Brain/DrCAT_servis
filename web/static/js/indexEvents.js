"use strict";

let pText = document.querySelector(".indexBackground > p");
let startHadler = document.getElementById("button-start");
let aTextStart = document.querySelector("#button-start > a");
startHadler.onmouseover = startHadler.onmouseout = startHandler;

function startHandler(event) {

  if (event.type == 'mouseover') {
    startHadler.style.width = "170px";
    startHadler.style.height = "57px";
    startHadler.style.marginLeft = "65px";
    pText.style.marginBottom = "14px";
    aTextStart.style.fontSize = "28px";
  }
  if (event.type == 'mouseout') {
    startHadler.style.width = "150px";
    startHadler.style.height = "50px";
    startHadler.style.marginLeft = "75px";
    pText.style.marginBottom = "16px";
    aTextStart.style.fontSize = "25px";
  }
}

let authButton = document.querySelector(".auth-buttons > input");
authButton.onmouseover = authButton.onmouseout = authHandler;

function authHandler(event) {

    if (event.type == 'mouseover') {
        authButton.style.width = "160px";
        authButton.style.height = "53px";
        authButton.style.marginTop = "30.5px";
        authButton.style.fontSize = "24px";
        authButton.style.marginBottom = "13.5px";
    }
    if (event.type == 'mouseout') {
        authButton.style.height = "50px";
        authButton.style.width = "150px";
        authButton.style.marginTop = "32px";
        authButton.style.fontSize = "22px";
        authButton.style.marginBottom = "15px";
    }
  }

let withoutButton = document.getElementById("button-without");
let whithoutA = document.querySelector("#button-without > a");
withoutButton.onmouseover = withoutButton.onmouseout = withoutButtonHandler;

function withoutButtonHandler(event) {
  if (event.type == 'mouseover') {
    withoutButton.style.width = "275px";
    withoutButton.style.height = "53px";
    withoutButton.style.marginTop = "33.5px";
    whithoutA.style.fontSize = "16px";
}
  if (event.type == 'mouseout') {
    withoutButton.style.width = "260px";
    withoutButton.style.height = "50px";
    withoutButton.style.marginTop = "35px";
    whithoutA.style.fontSize = "15px";
}
}