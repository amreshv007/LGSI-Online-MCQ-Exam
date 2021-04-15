$(document).ready(function(){
    $("#takenfrom").hide();
    $('#a').css('background', '#d25252');
    $('#a').css('color', 'white'); 
    $("#a").click(function(){
        $("#takenfrom").hide();
        $("#givento").show();
        $('#a').css('background', '#d25252');
        $('#a').css('color', 'white'); 
        $('#b').css('background', '#b3b2b25e');
        $('#b').css('color', 'black'); 
    });

    $("#b").click(function(){
        $("#givento").hide();
        $("#takenfrom").show();
        $('#b').css('background', '#d25252');
        $('#b').css('color', 'white'); 
        $('#a').css('background', '#b3b2b25e');
        $('#a').css('color', 'black'); 
    });
});
function checkinput(){
    let get_email = document.getElementById('email');
    let email = get_email.value;
    let pass1 = document.getElementById('password');
    let pass11 = pass1.value;
    let pass2 = document.getElementById('re_password');
    let pass22 = pass2.value;
    let email1 = email.split("@");
    if(email1[1] != "lge.com" || email1.length != 2){
        alert("Please Enter Correct Email ID!");
    }
    if(pass11 != pass22){
        alert("Password Mismatched!");
    }
}
function show_passwrd(){
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
function show_passwrd1(){
    let x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}
function show_passwrd2(){
    let y = document.getElementById("newpassword");
    if (y.type === "password") {
        y.type = "text";
    } else {
        y.type = "password";
    }
}