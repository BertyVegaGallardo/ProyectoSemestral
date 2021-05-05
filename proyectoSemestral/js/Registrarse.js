$(document).ready(function(){
    $('#show').mousedown(function(){
        $('#txtContrasenia').removeAttr('type');
    });

    $('#show').mouseup(function(){
        $('#txtContrasenia').atttr('type','password');
    });
});