from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import LgsiExam, UserAnswer, UserEmpId
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    return render(request,"screen1.html",{})

@login_required(login_url='/lgsi-mcq-exam/login')
def seresult(request):
    if request.user.is_superuser:
        se_result = UserAnswer.objects.filter(examtype="SE")
        allquestions = LgsiExam.objects.filter(examtype="SE")
        total_marks = 10*allquestions.count()
        all_user = User.objects.all()
        all_emp = UserEmpId.objects.all()
        se_result1 = []
        first_name = ""
        empid = ""
        email = ""
        for res in se_result:
            user1 = res.user
            marks = res.result
            for alluser in all_user:
                if alluser == user1:
                    first_name = alluser.first_name
                    email = alluser.email
                    break
            for emp in all_emp:
                if emp.user == user1:
                    empid = emp.emp_id
                    break
            percentage = int((int(marks)/int(total_marks))*100)
            if int(marks) < 0:
                percentage = 0
                marks = 0
            ob = {'first_name':first_name,'emp_id':empid,'result':marks,'percentage':percentage,'email':email}
            se_result1.append(ob)
        return render(request,"allresult.html",{'result_type':"SE",'se_result':se_result1,'total_marks':total_marks})

@login_required(login_url='/lgsi-mcq-exam/login')
def plresult(request):
    if request.user.is_superuser:
        pl_result = UserAnswer.objects.filter(examtype="PL")
        allquestions = LgsiExam.objects.filter(examtype="PL")
        total_marks = 10*allquestions.count()
        all_user = User.objects.all()
        all_emp = UserEmpId.objects.all()
        pl_result1 = []
        first_name = ""
        empid = ""
        email = ""
        for res in pl_result:
            user1 = res.user
            marks = res.result
            for alluser in all_user:
                if alluser == user1:
                    first_name = alluser.first_name
                    email = alluser.email
                    break
            for emp in all_emp:
                if emp.user == user1:
                    empid = emp.emp_id
                    break
            percentage = int((int(marks)/int(total_marks))*100)
            if int(marks) < 0:
                percentage = 0
                marks = 0
            ob = {'first_name':first_name,'emp_id':empid,'result':marks,'percentage':percentage,'email':email}
            pl_result1.append(ob)
        return render(request,"allresult.html",{'result_type':"PL",'pl_result':pl_result1,'total_marks':total_marks})

@login_required(login_url='/lgsi-mcq-exam/login')
def se_pl(request):
    if request.method == "GET":
        try:
            examtype = request.GET["examtype"]
        except:
            print("======== ")
            return redirect("/lgsi-mcq-exam")
        examtype.upper()
        if request.user.is_superuser:
            return render(request,"upload_ques.html",{'examtype':examtype})
        else:
            result1 = -2
            user_result = UserAnswer.objects.filter(user=request.user,examtype=examtype)
            allquestions = LgsiExam.objects.filter(examtype=examtype)
            total_marks = 10*allquestions.count()
            for res1 in user_result:
                result1 = -1
                if res1.result != -1:
                    result1 = int(res1.result)
                    req_scored = total_marks - result1
                    actual_prcntg = int((result1/total_marks)*100)
                    req_prcntg = int((req_scored/total_marks)*100)
                    return render(request,"pre_result1.html",{'examtype':examtype,'user_result':actual_prcntg,'req_scored':req_prcntg})
            if result1 == "-1":
                return render(request,"pre_result1.html",{'examtype':examtype,'user_result':result1})
            else:
                questions = LgsiExam.objects.filter(examtype = examtype)
                res = -1;
                user_ans = UserAnswer(user=request.user,result=res,examtype=examtype)
                user_ans.save()
                return render(request,"pl_se.html",{'examtype':examtype, 'questions':questions})
    else:
        return redirect("/lgsi-mcq-exam")

@login_required(login_url='/lgsi-mcq-exam/login')
def uploadq(request):
    if request.method == "POST":
        examtype = request.POST.get('examtype', None)
        allques = request.POST.get('allq', None)
        LgsiExam.objects.filter(examtype=examtype).delete()
        for ques in json.loads(allques):
            eachques = LgsiExam(user=request.user,question=ques['ques'],option1=ques['op1'],option2=ques['op2'],option3=ques['op3'],option4=ques['op4'],answer=ques['ans'],examtype=str(examtype))
            eachques.save()
            print("Saveddddddd")
        UserAnswer.objects.filter(examtype=examtype).delete()
        return redirect("/lgsi-mcq-exam")

def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        print("============= ",user)
        if user is not None:
            auth.login(request,user)
            return redirect("/lgsi-mcq-exam")
        else:
            messages.info(request, "Incorrect! Username or Password!")
            return redirect("/lgsi-mcq-exam/login")
    else:
        if request.user.is_authenticated:
            return redirect("/lgsi-mcq-exam")
        else:
            return render(request,"login2.html",context)

def signup(request):
    context = {}
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        emp_id = request.POST["emp_id"]
        username = request.POST["username"]
        password1 = request.POST["password"]
        password2 = request.POST["re_password"]
        email1 = email.split("@")
        if email1[1] != "lge.com" or len(email1) != 2:
        	if email1[1] != "lgepartner.com":
        		return redirect("/lgsi-mcq-exam/signup")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("User already exist!")
                messages.info(request,"User already exist!")
                return redirect("/lgsi-mcq-exam/signup")
            else:
                user1 = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user1.save()
                emp = UserEmpId(user=user1,emp_id=emp_id)
                emp.save()
                print("User created!")
                messages.info(request, "User created!")
                return redirect("/lgsi-mcq-exam/login")
        else:
            return HttpResponseRedirect(request.path_info)
    else:
        if request.user.is_authenticated:
            return redirect("/lgsi-mcq-exam")
        else:
            return render(request,"signup2.html",context)

@login_required(login_url='/lgsi-mcq-exam/login')
def result(request):
    if request.method == "POST":
        print("=====================")
        examtype = request.POST["examtype"]
        print(examtype)
        allquestions = LgsiExam.objects.filter(examtype=examtype)
        total_ans = 0
        i = 1
        ans = ""
        for ques in allquestions:
            q = "ques"+str(i)
            try:
                ans = request.POST[q]
            except:
                ans = "Wrong"
            i = i + 1
            print(ans)
            actual_ans = LgsiExam.objects.get(examtype=examtype,question=ques.question)
            print(actual_ans.answer)
            if actual_ans.answer == ans:
                total_ans = total_ans + 10;
        user_res = UserAnswer.objects.filter(examtype=examtype,user=request.user)
        allquestions = LgsiExam.objects.filter(examtype=examtype)
        total_marks = 10*allquestions.count()
        result1 = -1
        for res1 in user_res:
            if res1.result != "-1":
                result1 = int(res1.result)
                req_scored = total_marks - result1
                actual_prcntg = (result1/total_marks)*100
                req_prcntg = (req_scored/total_marks)*100
                return render(request, "pre_result2.html",{'user_result':actual_prcntg,'examtype':examtype,'req_scored':req_prcntg})
            res1.delete()
        user_ans = UserAnswer(user=request.user,result=total_ans,examtype=examtype)
        user_ans.save()
        actual_prcntg = int((total_ans/total_marks)*100)
        req_scored = total_marks - total_ans
        req_prcntg = int((req_scored/total_marks)*100)
        return render(request, "result.html",{'user_result':actual_prcntg, 'examtype':examtype,'req_scored':req_prcntg})
    else:
        return redirect("/lgsi-mcq-exam")

@login_required(login_url='/lgsi-mcq-exam/login')
def editProfile(request):
    return render(request, "edit-profile1.html")

@login_required(login_url='/lgsi-mcq-exam/login')
def editfname(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        getuser = User.objects.get(username=request.user.username);
        User.objects.filter(username=request.user).update(first_name=first_name)
    return redirect("/lgsi-mcq-exam/edit-profile")

@login_required(login_url='/lgsi-mcq-exam/login')
def editlname(request):
    if request.method == "POST":
        last_name = request.POST["last_name"]
        User.objects.filter(username=request.user).update(last_name=last_name)
    return redirect("/lgsi-mcq-exam/edit-profile")

@login_required(login_url='/lgsi-mcq-exam/login')
def editpassword(request):
    if request.method == "POST":
        curr_password = request.POST["currpassword"]
        new_password = request.POST["newpassword"]
        re_password = request.POST["re_password"]
        user_name = request.user.username
        user = auth.authenticate(username=user_name,password=curr_password)
        if user is not None:
            if new_password == re_password:
                # save the updated password.
                user.set_password(new_password)
                user.save()
                return redirect("/lgsi-mcq-exam/login")
            else:
                messages.info(request, "New Password Mismatched!")
                return HttpResponseRedirect(request.path_info)
        else:
            messages.info(request, "Enter Correct Current Password!")
    return redirect("/lgsi-mcq-exam/edit-profile")

@login_required(login_url='/lgsi-mcq-exam/login')
def logout(request):
    if request.method == "POST":
        auth.logout(request)
    return redirect("/lgsi-mcq-exam/")