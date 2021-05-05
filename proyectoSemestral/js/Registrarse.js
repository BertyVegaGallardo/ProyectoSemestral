$(document).ready(function(){
    $('#show').mousedown(function(){
        $('#txtContrasenia').removeAttr('type');
        $('#show').addClass('fa-eye-slash').removeClass('fa-eye');
    });

    $('#show').mouseup(function(){
        $('#txtContrasenia').attr('type','password');
        $('#show').addClass('fa-eye').removeClass('fa-eye-slash');
    });
});