from django.shortcuts import render,redirect
from django.http import HttpResponse
from e_public_app.models import Department,Peoples,Complaints
from django.contrib.auth import login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender=request.POST.get('gender')

        mobile_number=request.POST.get('mobile')
        aadhaar_number=request.POST.get('aadhaar')
        district=request.POST.get('district')
        legislative_assembly=request.POST.get('legestic')
        panchayath=request.POST.get('panchayath')
        pincord=request.POST.get('pincord')
    
        user, created = User.objects.get_or_create(username=username,password=password,email=email,first_name=first_name,last_name=last_name,is_staff=1)
        user, created = Peoples.objects.get_or_create(address=address,gender=gender,mobile_number=mobile_number,aadhaar_number=aadhaar_number,district=district,legislative_assembly=legislative_assembly,panchayath=panchayath,pincord=pincord,peoples=user)
        # peoples.user=user
        # peoples.address=address
        # peoples.gender=gender
        # peoples.mobile_number=mobile_number
        # peoples.aadhaar_number=aadhaar_number
        # peoples.district=district
        # peoples.legislative_assembly=legislative_assembly
        # peoples.panchayath=panchayath
        # peoples.pincord=pincord
        # peoples.save()
        return redirect("home")
    else:
        # return redirect("signup")
        return render(request,"user_sign_up.html")
    

def home(request):
    return render(request,"people_template/home_content.html")



def dep_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        place = request.POST.get('place')

        user=User.objects.create(username=username,password=password,email=email,first_name=first_name,is_staff=0)
        Department.objects.create(place=place)
        user.save()
        return redirect("dep_signup")

    else:
        return render(request,"admin_template/dep_signup.html")


def user_add_complaint(request):
    if request.method == 'POST':
        description=request.POST.get('description')
        department_id=request.POST.get('department')
        people_id=request.POST.get('user')

        departmentname_obj=Department.objects.get(id=department_id)
        people_obj=Peoples.objects.get(id=people_id)
        try:
            complaint=Complaints.objects.create(description=description,people_id=people_obj,department_id=departmentname_obj)

            complaint.save()
            messages.success(request, "Complaint senting successfully")
            return redirect("user_add_complaint")
        except:
            messages.error(request, "Failed to Sent Complaint!")
            return redirect("user_add_complaint")

        
    else:
        department=Department.objects.all()
        peoples=Peoples.objects.all()
        context = {
            "department":department,
            "peoples":peoples,
        }
        return render(request,"user_add_complaint.html",context)



def admin_home(request):
    return render(request,"admin_template/home_content.html")


def admin_view_complaints(request):
    complaints=Complaints.objects.all().order_by("-id")
    context={
        "complaints":complaints,
    }
    return render(request,"admin_template/admin_view_complaint.html",context)


def admin_approve_complaint(request,complaint_id):
    complaint=Complaints.objects.get(id=complaint_id)
    complaint.status=1
    complaint.save()
    return redirect("admin_view_complaints")

def admin_disapprove_complaint(request,complaint_id):
    complaint=Complaints.objects.get(id=complaint_id)
    complaint.status=2
    complaint.save()
    return redirect("admin_view_complaints")

def approved_complaints(request):
    complaints=Complaints.objects.all().order_by("-id")
    context={
        "complaints":complaints,
    }
    return render(request,"admin_template/approved_complaints.html",context)


def dep_login(request):
    if request.method != 'POST':
        

        return render(request,"department_template/dep_login.html")
        
    else:
        username = request.POST['username']
        password = request.POST['password']
        # user = auth.authenticate(username=username, password=password)
        # if user is not None:
        #     # if user.is_staff == 1:
        #     auth.login(request, user)
        #     return redirect('dep_home')
        #         #if user.is_staff == 1:
        #             #return redirect('/')
        #     # else:
        #         # messages.error(request, 'Invalid username and password')
        #         # return redirect("dep_login")
        # else:
        #     print("hi")
        #     return redirect("dep_login")

        # user=auth.authenticate(username=username,password=password)
        # print(request.POST.get('username'))
        # print(user)
        # if user != None:
        #     auth.login(request,user)
        #     # login(request,user)
        #     if user.is_staff=="0":
        #         return redirect("dep_home")
        # else:
        #     print("hi")

        #     return redirect("dep_login")\


        userdata = User.objects.get(username=username)
        if userdata.password == password:
            request.session['team'] = userdata.username
            return redirect('dep_home')
        else:
            return redirect('dep_login')


def dep_home(request):
    arshad = request.session['team']
    print(arshad)
    return render(request,"department_template/home_content.html",{'userdata':arshad})


def dep_view_complaint(request):
    arshad = request.session['team']
    print(arshad)
    user = User.objects.get(first_name=arshad)
    complaints = Complaints.objects.all()
    for co in complaints:
        print(co)
    return render(request,"department_template/view_complaint.html",{'userdata':arshad,'complaints':complaints})


def complaint_complete(request,complaint_id):
    complaint=Complaints.objects.get(id=complaint_id)
    complaint.status=2
    complaint.complete=1
    complaint.save()
    return redirect("dep_view_complaint")




def user_home(request):
    return render(request,"people_template/home_contet.html")



def user_complaint_status(request):
    complaints=Complaints.objects.all().order_by("-id")
    context={
        "complaints":complaints,
    }
    return render(request,"people_template/people_view_complaint.html",context)


def user_approve_solution(request,complaint_id):
    complaint=Complaints.objects.get(id=complaint_id)
    complaint.complete=3
    complaint.save()
    return redirect("user_complaint_status")
