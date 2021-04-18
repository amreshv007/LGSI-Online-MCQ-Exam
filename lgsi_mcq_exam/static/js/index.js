console.log("Welcomeeee");
function choose_exam_type(){
	var lang = document.getElementsByName('examtype');   
	let selected_lang = ""; //by Default       
    for(i = 0; i < lang.length; i++) { 
        if(lang[i].checked){
        	selected_lang = lang[i].value;
        	break;
    	}
    }
    // console.log(selected_lang);
    if(selected_lang === ""){
        alert("Please select the exam type!");
    }
}
// document.getElementById("min1").innerHTML = min+" Minutes";
function start_test() {
    let inst = document.getElementById("instruct");
    inst.style.display = "none";
    let quests = document.getElementById("quests");
    quests.style.display = "block";
    var time_in_minutes = 1;
    let min = 5;
    var current_time = Date.parse(new Date());
    var deadline = new Date(current_time + time_in_minutes*min*60*1000);
    run_clock('clockdiv',deadline);
}
let qcount = 1;
$("#add_ques").on('click', function(){
    qcount = qcount + 1;
    $("#allques").append('<div class="eachques"><li class="ad_ques"><input type="text" name="Ques" placeholder="Question_'+qcount+'"><button type="button" onclick="dlt_ques()" class="dlt_button">Delete</button></li><div class="OP"><input type="radio" name="Radio'+qcount+'"><input type="text" name="Option" placeholder="Option A"> <input type="radio" name="Radio'+qcount+'"> <input type="text" name="Option" placeholder="Option B"><br><input type="radio" name="Radio'+qcount+'"><input type="text" name="Option" placeholder="Option C"> <input type="radio" name="Radio'+qcount+'"><input type="text" name="Option" placeholder="Option D"><br></div><hr></div>');
});
function dlt_ques(){
    let els = document.getElementsByClassName("dlt_button");
    for (let i = 0; i < els.length; i++) {
        els[i].addEventListener('click', function (e) {
            e.preventDefault();
            e.target.closest('div.eachques').remove();
        });
    }
}
$('#uploadques').on('click', function(){
    // alert("hereeee");
    let qs = document.getElementsByName("Ques");
    let options = document.getElementsByName("Option");
    let allq = [];
    csrf = $('input[name=csrfmiddlewaretoken]').val();
    examtype = $('input[name=examtype]').val();
    // alert(csrf);
    for(let i=0;i<qs.length;i++){
        let radios = document.getElementsByName("Radio"+(i+1)+"");
        let ans = "";
        for(let j=0;j<4;j++){
            if(radios[j].checked){
                ans  = options[i*4+j].value;
            }
        }
        if(ans == ""){
            alert("Select Answer for Question "+(i+1));
            return;
        }
        let eachq = {
            'ques' : qs[i].value,
            'op1'  : options[i*4].value,
            'op2'  : options[i*4+1].value,
            'op3'  : options[i*4+2].value,
            'op4'  : options[i*4+3].value,
            'ans'  : ans,
        };
        allq.push(eachq);
    }
    console.log(allq);
    $.ajax({
        type: "POST",
        url: '../upload-question',
        data: {
                'csrfmiddlewaretoken' : csrf,
                'allq' : JSON.stringify(allq),
                'examtype' : examtype
            },
        dataType: "JSON",
        ContentType : 'application/x-www-form-urlencoded',
        success : function(data){
            alert("Successful");
        },
        failure : function(error){
            alert("Failure");
        }
    });
});
