from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from User.models import BasicDetails, FamilyMembers, DomesticAnimals, VegFru, Fish, Rubber,Survey
from django.contrib import messages
from . import validations
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def Login(request):
    if request.method == "POST":

        username = request.POST['email']
        password = request.POST['password']

        try:
            
            user = auth.authenticate(username=username,password=password)
           
        except:
            user = None

        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
           
            return redirect("Home")

        else:
           #messages.success(request,'Incorrect Username or Password!')
           #print("Incorrect Username or Password!")
           return render(request,'Login.html')
    
    else:
        return render(request, 'Login.html')


def Logout(request):
    logout(request)
    return render(request,'Login.html')


@login_required(login_url='/Login')
def Passwordupdate(request):
    if request.method == "POST":
        username = request.session['username']
        current = request.POST['oldpsw']
        New = request.POST['psw']

        try:
            user = auth.authenticate(username=username,password=current)
           
        except:
            
            user = None
        
        if user is not None :
            user.set_password(New)
            user.save()
            #print("Password Updated")
            return render(request,'Login.html')
        else:
            messages.success(request,'Current Password Entered Incorrect!')
            return render(request,'Passwordchange.html')
        
    else:
        return render(request, 'Passwordchange.html')


@login_required(login_url='/Login')
def Home(request):
    return render(request, 'Home.html')


@login_required(login_url='/Login')
def Profile_Home(request):
    if request.method == "GET":
        Id = request.GET['AuthId']
        try:
            num = BasicDetails.objects.filter(Auth_Id=Id).count()
        except:
            num = 0

        if num == 0:
            #print("No Records Found")
            messages.success(
                request, 'Sorry Records Not Found With Auth Id -' + Id)
            return render(request, 'Home.html')
        else:
            Auth = Id
            request.session['Auth'] = Id
            Profile = BasicDetails.objects.get(Auth_Id=Auth)
            Family = FamilyMembers.objects.filter(Auth_Id=Auth)
            Rub = Rubber.objects.filter(Auth_Id=Auth)
            Fish_Data = Fish.objects.filter(Auth_Id=Auth)
            domestic = DomesticAnimals.objects.filter(Auth_Id=Auth)
            Veg = VegFru.objects.filter(Auth_Id=Auth)
            survy = Survey.objects.filter(Auth_Id=Auth)
            return render(request, 'Profile_Home.html', {'Profile': Profile, 'Family': Family, 'Rub': Rub,
                                                         'Fish_Data': Fish_Data, 'Veg': Veg,'Animl':domestic,
                                                         'survy':survy})
    else:
        return render(request, 'Home.html')


@login_required(login_url='/Login')
def Main_Home(request):
    Auth = request.session['Auth']
    Profile = BasicDetails.objects.get(Auth_Id=Auth)
    Family = FamilyMembers.objects.filter(Auth_Id=Auth)
    Rub = Rubber.objects.filter(Auth_Id=Auth)
    Fish_Data = Fish.objects.filter(Auth_Id=Auth)
    Veg = VegFru.objects.filter(Auth_Id=Auth)
    domestic = DomesticAnimals.objects.filter(Auth_Id=Auth)
    survy = Survey.objects.filter(Auth_Id=Auth)

    return render(request, 'Profile_Home.html', {'Profile': Profile, 'Family': Family, 'Rub': Rub,
                                                 'Fish_Data': Fish_Data, 'Veg': Veg,'Animl':domestic,
                                                 'survy':survy})

# Insertion Start Here

@login_required(login_url='/Login')
def Profile(request):
    if request.method == 'POST':
        Auth_Id = request.POST['aadhar']
        Type = request.POST['Type']
        Name = request.POST['name']
        House = request.POST['house']
        Parish = request.POST['parish']
        Village = request.POST['village']
        Panch_Muns = request.POST['muncipality']
        District = request.POST['district']
        Phone = request.POST['phone']
        Email = request.POST['email']
        Occupation = request.POST['occupation']
        Created_Date = datetime.now()

        request.session['Auth'] = Auth_Id

        try:
            number = BasicDetails.objects.filter(Auth_Id=Auth_Id).count()
        except:
            number = 1

        if number == 1:
            #print("Records Found")
            messages.error(request,"This person already exists in our system")
            return render(request, 'Basic_Details.html')
        else:
            if validations.isNotEmpty(Authid=Auth_Id, type=Type, name=Name, house=House, parish=Parish, village=Village, panchayath=Panch_Muns, district=District, phone=Phone, email=Email, occupation=Occupation, createddate=Created_Date):
                Basic = BasicDetails(Auth_Id=Auth_Id, Type=Type, Name=Name, House=House, Parish=Parish, Village=Village,
                                     Panch_Muns=Panch_Muns, District=District, Phone=Phone, Email=Email, Occupation=Occupation, Farming='NA',
                                     Rubber='NA', DomesticAnimals='NA', VegFru='NA', Fish='NA', Created_Date=Created_Date)

                Basic.save()

                messages.success(
                    request, 'Profile Created Successfully Auth Id is - ' + Auth_Id)

                return redirect('Main_Home')
            else:
                messages.error("Please check if all data is correct")

    else:
        return render(request, 'Basic_Details.html')


@login_required(login_url='/Login')
def Family(request):

    if request.method == 'POST':
        Auth_Id = request.session['Auth']
        Name = request.POST['othersname']
        Relationship = request.POST['relationship']
        Blood = request.POST['bloodgroup']
        Job = request.POST['job']
        Phone = request.POST['phone']

        request.session['Auth'] = Auth_Id
        if validations.isNotEmpty(authid=Auth_Id, name=Name, relationship=Relationship, blood=Blood, job=Job, phone=Phone):
            Fammebers = FamilyMembers(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id), Name=Name, Relationship=Relationship, Blood=Blood,
                                      Job=Job, Phone=Phone)

            Fammebers.save()

            messages.success(request, 'Family Details Added')

            return redirect('Main_Home')
        else:
            messages.error(request, 'Sever side valiadtion failed...')
            return redirect('Main_Home')

    else:
        return render(request, 'Family_Details.html')


@login_required(login_url='/Login')
def Rubber_Farm(request):

    if request.method == 'POST':
        Auth_Id = request.session['Auth']
        Land_Area = request.POST['rubberland']
        Count = request.POST['rubbercount']
        Income = request.POST['latex']
        Rubber_Sheet = request.POST['rubbersheet']
        Rubber_Board = request.POST['membership']

        request.session['Auth'] = Auth_Id

        if validations.isNotEmpty(authid=Auth_Id, landarea=Land_Area, count=Count, income=Income, rubbersheet=Rubber_Sheet, rubberboard=Rubber_Board):
            Rub = Rubber(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id), Land_Area=Land_Area,
                         Count=Count, Income=Income, Rubber_Sheet=Rubber_Sheet, Rubber_Board=Rubber_Board)
            Rub.save()

            data = "Rubber_Farm"
            if validations.Tableupdate(data,request.session['Auth']):
                # print("updated")

                messages.success(request, 'Rubber Farming Details Added')
            return redirect('Main_Home')
        else:
            messages.error(request, 'Sever side valiadtion failed...')
            return redirect('Main_Home')

    else:
        return render(request, 'Rubber_Details.html')

@login_required(login_url='/Login')
def Animal(request):

    if request.method == 'POST':
        Auth_Id = request.session['Auth']
        Category = request.POST['animaltype']
        Count = request.POST['animalcount']
        Income = request.POST['animalincome']
        Marketing = request.POST['animalmarketing']
        Weed = request.POST['animalbreed']
        More_Space = request.POST['animalcapacity']
        More_Intrest = request.POST['animalinterest']

        request.session['Auth'] = Auth_Id

        if validations.isNotEmpty(authid=Auth_Id, category=Category, count=Count, income=Income, marketing=Marketing, breed=Weed, morespace=More_Space, moreinterest=More_Intrest):
            anmfarm = DomesticAnimals(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id), Category=Category, Count=Count,
                                      Income=Income, Marketing=Marketing, Weed=Weed, More_Space=More_Space, More_Intrest=More_Intrest)
            anmfarm.save()

            data = "Animal_Farm"
            if validations.Tableupdate(data,request.session['Auth']):
                # print("updated")

                messages.success(request, 'Animal Farming Details Added')
            return redirect('Main_Home')
        else:
            messages.error(request, 'Sever side valiadtion failed...')
            return redirect('Main_Home')

    else:
        return render(request, 'Animal_Details.html')


@login_required(login_url='/Login')
def Veg_Fru(request):

    if request.method == 'POST':
        Auth_Id = request.session['Auth']
        Category = request.POST['vegtype']
        Land_Area = request.POST['vegland']
        Income = request.POST['vegincome']
        Marketing = request.POST['vegmarketing']
        Weed = request.POST['vegbreed']
        More_Space = request.POST['vegcapacity']
        More_Intrest = request.POST['veginterest']

        request.session['Auth'] = Auth_Id
        if validations.isNotEmpty(authid=Auth_Id, category=Category, landarea=Land_Area, Income=Income, Marketing=Marketing, Breed=Weed, More_Space=More_Space, More_Intrest=More_Intrest):
            Veg = VegFru(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id), Category=Category, Land_Area=Land_Area,
                        Income=Income, Marketing=Marketing, Weed=Weed, More_Space=More_Space, More_Intrest=More_Intrest)

            Veg.save()

            data = "Veg_Farm"
            if validations.Tableupdate(data,request.session['Auth']):
                # print("updated")

                messages.success(request, 'Vegetable Details Added')

            return redirect('Main_Home')
        else:
            messages.error(request, 'Sever side valiadtion failed...')
            return redirect('Main_Home')


    else:
        return render(request, 'Vegetable_Fruit_Detail.html')

@login_required(login_url='/Login')
def Fish_Farm(request):

    if request.method == 'POST':
        Auth_Id = request.session['Auth']
        Category = request.POST['fishtype']
        Land_Area = request.POST['fishland']
        Method = request.POST['method']
        Income = request.POST['fishincome']
        Marketing = request.POST['fishmarketing']
        More_Space = request.POST['fishcapacity']
        More_Intrest = request.POST['fishinterest']

        request.session['Auth'] = Auth_Id

        if validations.isNotEmpty(authid=Auth_Id, Category=Category, Land_Area=Land_Area,
                         Method=Method, Income=Income, Marketing=Marketing, More_Space=More_Space, More_Intrest=More_Intrest):

            Fish_farm = Fish(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id), Category=Category, Land_Area=Land_Area,
                            Method=Method, Income=Income, Marketing=Marketing, More_Space=More_Space, More_Intrest=More_Intrest)

            Fish_farm.save()

            data = "Fish_Farm"
            if validations.Tableupdate(data,request.session['Auth']):
                # print("updated")

                messages.success(request, 'Fish Farming Details Added')

            return redirect('Main_Home')
        else:
            messages.error(request, 'Sever side valiadtion failed...')
            return redirect('Main_Home')


    else:
        return render(request, 'Fish_Detail.html')

# Updation Start Here

@login_required(login_url='/Login')
def updateFamily(request):
    if request.method== "GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = FamilyMembers.objects.get(id=id)
        return render(request, 'Update_Family.html',{ 'response':response })
    elif request.method == "POST":
        data = FamilyMembers.objects.get(id=request.session['fieldkey'])
        data.Name = request.POST['othersname']
        data.Relationship = request.POST['relationship']
        data.Blood = request.POST['bloodgroup']
        data.Job = request.POST['job']
        data.Phone = request.POST['phone']
        data.save()
        return redirect('Main_Home')


@login_required(login_url='/Login')
def updateRubber(request):
    if request.method=="GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = Rubber.objects.get(id=id)
        return render(request, 'Update_Rubber.html',{ 'response':response })
    elif request.method == "POST":
        data = Rubber.objects.get(id=request.session['fieldkey'])
        data.Land_Area = request.POST['rubberland']
        data.Count = request.POST['rubbercount']
        data.Income = request.POST['latex']
        data.Rubber_Sheet = request.POST['rubbersheet']
        data.Rubber_Board = request.POST['membership']
        data.save()
        return redirect('Main_Home')


@login_required(login_url='/Login')
def updateFish(request):
    if request.method=="GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = Fish.objects.get(id=id)
        return render(request, 'Update_Fish.html',{ 'response':response })
    elif request.method == "POST":
        data = Fish.objects.get(id=request.session['fieldkey'])
        data.Category = request.POST.get('fishtype')
        data.Land_Area = request.POST['fishland']
        data.Method = request.POST.get('method')
        data.Income = request.POST.get('fishincome')
        data.Marketing = request.POST.get('fishmarketing')
        data.More_Space = request.POST.get('fishcapacity')
        data.More_Intrest = request.POST.get('fishinterest')
        data.save()
        return redirect('Main_Home')


@login_required(login_url='/Login')
def updateDomestic(request):
    if request.method=="GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = DomesticAnimals.objects.get(id=id)
        return render(request, 'Update_Animal.html',{ 'response':response })
    elif request.method == "POST":
        data = DomesticAnimals.objects.get(id=request.session['fieldkey'])
        data.Category = request.POST.get('animaltype')
        data.Count = request.POST['animalcount']
        data.Income = request.POST.get('animalincome')
        data.Marketing = request.POST.get('animalmarketing')
        data.Weed = request.POST.get('animalbreed')
        data.More_Space = request.POST.get('animalcapacity')
        data.More_Intrest = request.POST.get('animalinterest')
        data.save()
        return redirect('Main_Home')


@login_required(login_url='/Login')
def updateVegFru(request):
    if request.method=="GET":
        id = request.GET['fieldkey']
        request.session['fieldkey'] = id
        response = VegFru.objects.get(id=id)
        return render(request, 'Update_Veg.html',{ 'response':response })
    elif request.method == "POST":
        data = VegFru.objects.get(id=request.session['fieldkey'])
        data.Category = request.POST['vegtype']
        data.Land_Area = request.POST['vegland']
        data.Income = request.POST['vegincome']
        data.Marketing = request.POST['vegmarketing']
        data.Weed = request.POST['vegbreed']
        data.More_Space = request.POST['vegcapacity']
        data.More_Intrest = request.POST['veginterest']
        data.save()
        return redirect('Main_Home')


@login_required(login_url='/Login')
def updateprofile(request):
    if request.method=="GET":
        id = request.session['Auth']
        response = BasicDetails.objects.get(Auth_Id=id)
        return render(request, 'Update_Profile.html',{ 'response':response })
    elif request.method == "POST":
        data = BasicDetails.objects.get(Auth_Id=request.session['Auth'])
        data.House = request.POST['house']
        data.Parish = request.POST['parish']
        data.Village = request.POST['village']
        data.Panch_Muns = request.POST['muncipality']
        data.District = request.POST['district']
        data.Phone = request.POST['phone']
        data.Email = request.POST['email']
        data.Occupation = request.POST['occupation']
        data.save()
        return redirect('Main_Home')

@login_required(login_url='/Login')
def deleteprofile(request):
    if 'profile' in request.POST:
        Id = request.POST['adhr']
        BasicDetails.objects.filter(Auth_Id=Id).delete()
        messages.success(request,'Profile Deleted Associated With Aadhar : ' + Id)
        return redirect('Home')
    elif 'family' in request.GET:
        Id = request.GET['key'] 
        FamilyMembers.objects.filter(id=Id).delete()
        messages.success(request,'Family Data Deleted')
        return redirect('Main_Home')
    elif 'rubber' in request.GET:
        Id = request.GET['key'] 
        Rubber.objects.filter(id=Id).delete()
        messages.success(request,'Rubber Data Deleted')
        return redirect('Main_Home')
    elif 'animal' in request.GET:
        Id = request.GET['key'] 
        DomesticAnimals.objects.filter(id=Id).delete()
        messages.success(request,'Animal Farm Data Deleted')
        return redirect('Main_Home')
    elif 'fish' in request.GET:
        Id = request.GET['key'] 
        Fish.objects.filter(id=Id).delete()
        messages.success(request,'Fish Farm Data Deleted')
        return redirect('Main_Home')
    elif 'veg' in request.GET:
        Id = request.GET['key'] 
        VegFru.objects.filter(id=Id).delete()
        messages.success(request,'Vegitables Farm Data Deleted')
        return redirect('Main_Home')
    else:
        return render(request,'Profile_Home.html')



@login_required(login_url='/Login')
def Survey_Data(request):
    if request.method == "POST":
        Auth_Id = request.session['Auth']
        Intrest = request.POST['jobbank']
        Jobs = request.POST.getlist('jobs')
        Business = request.POST.getlist('business')
        News_Paper = request.POST.getlist('newspaper')

        data = Survey(Auth_Id=BasicDetails.objects.get(Auth_Id=Auth_Id),Intrest=Intrest,Jobs=Jobs,
        Business=Business,News_Paper=News_Paper)

        data.save()

        messages.success(request, 'Survey Form Submitted Successfully')

        return redirect('Main_Home')
    else:
        return render(request, 'Survey.html')


@login_required(login_url='/Login')
def Contact(request):
    return render(request, 'Contact.html')


# Errror Handling Pages


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
