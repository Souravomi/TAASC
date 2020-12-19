import phonenumbers
from User.models import BasicDetails
from django.shortcuts import render

# Validating phone number returns true or false 
def validatePhone(ph):
    return phonenumbers.is_valid_number(phonenumbers.parse(str(ph), "IN"))

#validate UID
def validateUID(uid):
    if str(uid).isnumeric() and len(str(uid))==12:
        return True
    return False

#validate if any field is empty
def isNotEmpty(**args):
    for k,v in args.items():
        if v==None or v=='':
            print(f'please check the value for {k}'.format(k))
            return False
    return True

def Tableupdate(table,id):
    main = BasicDetails.objects.get(Auth_Id=id)
    main.Farming = "Yes"
    main.save()
    if table == "Rubber_Farm":
        main = BasicDetails.objects.get(Auth_Id=id)
        main.Rubber = "Yes"
        main.save()
        return True
    elif table == "Veg_Farm":
        main = BasicDetails.objects.get(Auth_Id=id)
        main.VegFru = "Yes"
        main.save()
        return True
    elif table == "Fish_Farm":
        main = BasicDetails.objects.get(Auth_Id=id)
        main.Fish = "Yes"
        main.save()
        return True
    elif table == "Animal_Farm":
        main = BasicDetails.objects.get(Auth_Id=id)
        main.DomesticAnimals = "Yes"
        main.save()
        return True
    else:
        return False





