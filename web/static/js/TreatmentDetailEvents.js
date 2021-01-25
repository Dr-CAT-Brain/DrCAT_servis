let setActive = false;
let leavingTime = 200;
$('#sidebar').toggleClass('active');

$(document).ready(function () {
    $('#previousButton').on('click', () => {
        window.history.back();
    })

    $('#sidebarCollapse').on('click', function () {``
        $('#sidebar').toggleClass('d-none');

        document.getElementById("open-buttons").style.zIndex = "-1"
        document.getElementById("data").style.display = "block";
        document.getElementById("simular").style.display = "none";

        setTimeout(function(){
          $('#sidebar').toggleClass('active');
          }, 10);
    });

    $('#sidebarCollapse2').on('click', function () {
        $('#sidebar').toggleClass('active');
        document.getElementById("open-buttons").style.zIndex = "1";
        setTimeout(function(){
          $('#sidebar').toggleClass('d-none');
          }, leavingTime);
    });

    $('#simularCollapse').on('click', function () {
        $('#sidebar').toggleClass('d-none');

        document.getElementById("open-buttons").style.zIndex = "-1";
        document.getElementById("data").style.display = "none";
        document.getElementById("simular").style.display = "block";

        setTimeout(function(){
          $('#sidebar').toggleClass('active');
          }, 10);
    });

    $('#simularCollapse2').on('click', function () {
        $('#sidebar').toggleClass('active');

        document.getElementById("open-buttons").style.zIndex = "1";
        document.getElementById("data").style.display = "none";
        document.getElementById("simular").style.display = "block";

         setTimeout(function(){
          $('#sidebar').toggleClass('d-none');
          }, leavingTime);
    });
});

let isOpen = false;

function imgFullScreenOpen(target) {
    $("#imgFullScreen > img").attr("src", target.children[0].src);

    document.getElementById("imgFullScreen").style.display = "flex"
    document.getElementById("imgFullScreen").style.opacity = "1";

    isOpen = !isOpen;
}

function imgFullScreenClose(target) {
    if (isOpen) {
        target.style.opacity = "0";
        setTimeout(() => target.style.display = "none", 200);
        isOpen = !isOpen;
    }
}