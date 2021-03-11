from django.shortcuts import render,redirect, HttpResponseRedirect
from app.models import Signup, Form1, Form2

# Create your views here.

def home(request):
    return render(request,"home.html")
def signup(request):
    if request.method=='POST':
        phone=request.POST['phone']
        email=request.POST['email']
        age=request.POST['age']
        password=request.POST['password']
        instance=Signup(phone=phone,email=email,age=age, password=password)
        instance.save() 
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")   

            
    return render(request,"signup.html")
def login(request):
    import sqlite3
    if request.method=="POST":
       phone1=request.POST['phone']
       password1=request.POST['password']
       Connection=sqlite3.connect("db.sqlite3")
       crsr=Connection.cursor()
       crsr.execute("SELECT*FROM app_signup")
       ans=crsr.fetchall()
       #print(ans)
       for i in range(len(ans)):
           if ans[i][2]==phone1 and ans[i][3]==password1:
               return HttpResponseRedirect("http://127.0.0.1:8000/form1/")
           
       return HttpResponseRedirect("http://127.0.0.1:8000/signup/")

    return render(request,"login.html") 
def form1(request):
    if request.method=="POST":
         area=request.POST['area']
         t_person=request.POST['t_person'] 
         leads=request.POST['leads']
         instance=Form1(area=area, t_person=t_person, leads=leads)
         instance.save()
         return HttpResponseRedirect("http://127.0.0.1:8000/form2/")
    return render(request,"form1.html") 

def form2(request):
    import sqlite3
    Connection=sqlite3.connect("db.sqlite3")
    crsr=Connection.cursor()
    crsr.execute("SELECT t_person FROM app_form1 where id=(select count(t_person) from app_form1)")
    ans=crsr.fetchall()
    print(ans)
    l=list(range(1,ans[0][0]+1))
    print(l)
    context={"loop":l}
    if request.method=="POST":
       name=request.POST['name']
       dob=request.POST['dob']
       gender=request.POST['gender']
       age=request.POST['age']
       members=request.POST['members']
       instance=Form2(name=name,dob=dob,gender=gender,age=age,members=members)
       instance.save()
      
           

    return render(request,"form2.html",context)  
def edit(request):
    stud=Form2.objects.all()
    return render(request,"edit.html",{"stu":stud})    
def updatedata(request,id):
    if request.method=="POST":
      
       name=request.POST['name']
       dob=request.POST['dob']
       gender=request.POST['gender']
       age=request.POST['age']
       members=request.POST['members']
       instance=Form2(name=name,dob=dob,gender=gender,age=age,members=members,id=id)
       instance.save()
       

    return render(request,"update.html",{"id":id})       