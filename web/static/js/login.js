$('#login_btn').click(function() {
  var username = $.trim($('#id_username').val());
    var pwd = $.trim($('#id_password').val());
    var stayloggedIn = true;
    $.ajax({
        url: "api/login/",
        type: "post",
        data: {
            username: username,
            pwd: pwd,
            csrfmiddlewaretoken: $('#csrf_token').data("content"),
            stayloggedIn: stayloggedIn,
        }
    }).done(function(data) {
        if (data == 'Success'){
            window.location.href = window.location.href.replace('login', 'cabinet');
        }
//        alert(data);
    });
});