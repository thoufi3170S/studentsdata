from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from members.models import member,destinaton,od_form


# Create your views here.
def login(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    print("*************pass entered*********************")
    print(username)
    print(password)
    
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request, user)
      print("************************user verified************************************")
      return redirect('home')
    else:
      print("******************user missmatched ******************************")
      messages.info(request,'invalid credentiial')
      return redirect('login')
      
  
  else: 
    return render(request,'login.html')
  
###############################################################################################################  
def register(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username  = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    email = request.POST['email']
    
    if password1 == password2:
      user = User.objects.create_user(username=username , password=password1 , email=email , first_name=first_name , last_name=last_name)
      user.save()
      print('user created')
      return render(request,'login.html')
      
    else:
      print("password is'nt match...")
      return render(request,'register.html')
  
      

  else:
    return render(request,'register.html')
  ##########################################################################################
def logout(request):
  auth.logout(request)
  return redirect('/')
############################################################################################
def studata(request):
   stud = member.objects.all()
   context = {
    'stud' : stud
   }
   print(context)
   return render(request,'studentdata.html',context)
##############################################################################################
def drop(request):
  if request.method == "POST":
    register = request.POST['register']
    data = member.objects.get(registerno=register)
    data.delete()
    return HttpResponse("deleted successfully")
  else:
    return render(request,'drop.html')
  #############################################################################################
def adddata(request):
    if request.method == 'POST':
        # Retrieve form data
        id = request.POST['id']
        name = request.POST['name']
        gender = request.POST['gender']
        registerno = request.POST['registerno']
        idno = request.POST['idno']
        aadharno = request.POST['aadharno']
        year = request.POST['year']
        image = request.FILES['image']  
        
 # ##########Create a new member object#########
        data = member(
            id=id,
            name=name,
            gender=gender,
            registerno=registerno,
            idno=idno,
            aadharno=aadharno,
            year=year,
            image=image  
        )
        
     
        data.save()
        return HttpResponse("Data added successfully")
    else:
        return render(request, 'adddata.html')
    ########################################################################################
def filter(request):
  if request.method == 'POST':
     register = request.POST['register']
     gender = request.POST['gender']
     year = request.POST['year']
     data = member.objects.all()
     if register:
       data = data.filter(registerno=register)
       context ={
          'data': data
        }
     if gender:
       data = data.filter(gender=gender)
       context ={
          'data': data
        }
     if year:
       data = data.filter(year=year)
       context ={
          'data': data
        }
     return render(request,'filtered.html',context)
  else:
    return render(request,'filter.html')
  ##############################################################################################
def alumini(request):
   alumi = destinaton.objects.all()
   context = {
    'alumi' : alumi
   }
   print(context)
   return render(request,'alumini.html',context)
###############################################################################################
def odrequest(request):
  
  if request.method == 'POST':
    register =  request.POST.get('registerno')
    defined_register=int(register)
    idno=request.POST.get('idno')
    defined_idno =str(idno)
    data=member.objects.all()
    try:    
            my_object = data.filter(registerno=defined_register)
            for reg in my_object:
              exact1=reg.registerno
              exact_register=int(exact1)
              exact2=reg.idno
              exact_idno=str(exact2)
              print(exact_register)
              print(exact_idno)
              print("user defined_register",defined_register)
              print("user defined_idno",defined_idno)
            
            # Do something if the object is found
            if exact_register == defined_register and exact_idno==defined_idno:
              print("in if condition")
              return render(request,'od.html')
              
            else:
              print("mudiyala da")
    except :
            # Do something if the object is not found
            return HttpResponse("not found")
          
  return render(request,'odrequest.html')
################################################################################################
def odform(request):
  if request.method == 'POST':
    name = request.POST['name']
    idno = request.POST['idno']
    department_name = request.POST['department_name']
    type_of_od = request.POST['type_of_od']
    reason = request.POST['reason']
    duration = request.POST['duration']
    class_incharge_name = request.POST['class_incharge_name']
    staff_id = request.POST['staff_id']
    data=od_form(name=name,idno=idno,department_name=department_name,type_of_od=type_of_od,reason=reason,duration=duration,class_incharge_name=class_incharge_name,staff_id=staff_id)
    data.save()
    return HttpResponse ("OD request submitted successfully.")
  return render(request,'blank.html')
 
       
  
  







