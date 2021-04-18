// 5 minutes from now
function time_remaining(endtime){
    var t = Date.parse(endtime) - Date.parse(new Date());
    var seconds = Math.floor( (t/1000) % 60 );
    var minutes = Math.floor( (t/1000/60) % 60 );
    var hours = Math.floor( (t/(1000*60*60)) % 24 );
    var days = Math.floor( t/(1000*60*60*24) );
    return {'total':t, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds};
    }

function run_clock(id,endtime){
    var clock = document.getElementById(id);
    function update_clock(){
        var t = time_remaining(endtime);
        clock.innerHTML = "<b>Time Remaining -</b> "+t.minutes+' M : '+t.seconds+' S';
        if(t.total<=0){
            clearInterval(timeinterval);
            console.log("Hereeeeeeeeeeeeeeeee");
            document.getElementById("button_lang").click();
        }
    }
    update_clock(); // run function once at first to avoid delay
    var timeinterval = setInterval(update_clock,1000);
}