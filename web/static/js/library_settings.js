"use strict";
$("#sidebar").toggleClass("active");

let previous2 = null;

function openSideBar() {
    $("#sidebar").toggleClass("d-none");

    setTimeout(() => $("#sidebar").toggleClass("active"), 10);
}

function closeSideBar() {
    $("#sidebar").toggleClass("active");

    setTimeout(() => $("#sidebar").toggleClass("d-none"), 100);
}

function setActive2(target) {
    if(previous2 != null){
        $(previous2).toggleClass('active');
    }
    $(target).toggleClass('active');
    previous2 = target;
}

let previous3 = null;

function setActive3(target) {
    if(previous3 != null){
        $(previous3).toggleClass('active');
    }
    $(target).toggleClass('active');
    previous3 = target;
}