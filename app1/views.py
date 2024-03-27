from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
import datetime
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_protect
from datetime import timedelta
from django.utils import timezone

# Now you can use timezone in your code



# Create your views here.
leave_data=0

#####New Merged#########
all_medicines =0
lab_investigation_report=0
kco = []
advice = []
all_medicines =[]
get_patient_by_appointment_id = []
insert_patient_vitals = []
get_patient_boimterics_vitals =[]
#doctor_id = {"doctor_id":"1"}
patient_biometric_id= 0
data1 = []
patient_info = []
consultation =[]


def opdlogin(request,token):
    print(token)
    api_data={"doctor_login_token":token}
    # api_url="http://127.0.0.1:8000/api/get_doctor_profileby_token/"
    api_url="http://13.233.211.102/doctor/api/get_doctor_profileby_token/"
    response=requests.post(api_url,json=api_data)
    if(response.json().get("message_code") ==999):
        request.session.clear()
        request.session['token']=token
        return redirect(doctorReg)
    else:
        doctor_id=response.json().get("message_data").get("doctor_id")
        api_data={"doctor_id":doctor_id}
        # api_url="http://127.0.0.1:8000/api/get_doctor_related_info/"
        api_url="http://13.233.211.102/doctor/api/get_doctor_related_info/"
        response=requests.post(api_url,json=api_data)
        all_id=response.json()
        request.session['doctor_id']=doctor_id
        request.session['location_id']=all_id.get('doctor_location_id')
        request.session['avalibility_id']=all_id.get('last_availability_id')
        request.session['medic_id']=all_id.get('last_medical_service_fee_id')
        request.session['consult_id']=all_id.get('last_consultation_fee_id')
        request.session.save()
        return redirect(dashboard)

    
def opdlogin1(request):
    return render(request,"Doctor/opdlogin.html")


def doctorReg(request):
    if(request.method=="GET"):
        # request.session['doctor_id'] =1
        # doctor_id=request.session['doctor_id']
        # print(request.session['doctor_id'])
        # request.session.clear()
        if 'doctor_id' in request.session:
            doctor_id=request.session['doctor_id']
            api_data={"doctor_id":doctor_id}
            # api_url="http://127.0.0.1:8000/api/get_doctor_by_id/"
            api_url="http://13.233.211.102/doctor/api/get_doctor_by_id/"
            response=requests.post(api_url,json=api_data)
            data=response.json().get("message_data",{})
            print(data)
            # Convert epoch timestamp to formatted date
            epoch_timestamp = data[0].get('doctor_dateofbirth', 0)
            # print(epoch_timestamp)
            # formatted_date = datetime.utcfromtimestamp(epoch_timestamp).strftime('%Y-%m-%d')
            formatted_date=datetime.datetime.fromtimestamp(epoch_timestamp).strftime( "%Y-%m-%d")   
            # print(formatted_date)
            data[0]['doctor_dateofbirth'] = formatted_date
            return render(request,"Doctor/DoctorRegUpdate.html",{"data":data[0],'doctor_id':doctor_id})
        else:
            request.session['doctor_id']=None
            return render(request,"Doctor/DoctorRegUpdate.html",{"doctor_id":None})
    
    else:
        doctor_id= request.session['doctor_id']
        fname=request.POST['firstName']
        lname=request.POST['lastName']
        regno=request.POST["registrationNumber"]
        aadharNumber=request.POST["aadharNumber"]
        pincode=request.POST["pincode"]
        city=request.POST["city"]
        state=request.POST["state"]
        country=request.POST["country"]
        address=request.POST["address"]
        dob=request.POST["dob"]
        mstatus=request.POST["maritalStatus"]
        gender=request.POST["gender"]
        email=request.POST["email"]
        mno=request.POST["mobileNumber"]
        api_data={
                "doctor_firstname": fname,
                "doctor_lastname": lname,
                "doctor_mobileno": mno,
                "doctor_email":email,
                "doctor_dateofbirth": dob,
                "doctor_maritalstatus":mstatus,
                "doctor_gender":gender,
                "doctor_aadharnumber": aadharNumber,
                "doctor_address": address,
                "doctor_cityid": 1,
                "doctor_stateid": 1,
                "doctor_countryid": 1,
                "doctor_pincode": pincode,
                "doctor_registrationno": regno,
                "isactive": 1,
                # "doctor_login_token":request.session['token']
            }
        # print(dob)
        if doctor_id is not None :
            update_data={
                "doctor_id": doctor_id,
                "updated_data":api_data
            }
            # api_url="http://127.0.0.1:8000/api/update_doctor_details/"
            api_url="http://13.233.211.102/doctor/api/update_doctor_details/"
            response=requests.post(api_url,json=update_data)
            messages.success(request, 'Doctor Profile updated successfully!')
            return redirect(settingdashboard)
        
        else:
            api_data['doctor_login_token']=request.session['token']
            # api_url = "http://127.0.0.1:8000/api/insert_doctor/"
            api_url = "http://13.233.211.102/doctor/api/insert_doctor/"

            response = requests.post(api_url, data=api_data)
            api_response = response.json()

            # Extract doctor_id from the response
            doctor_id = api_response.get("message_data", {}).get("doctor_id")
            request.session['doctor_id'] = doctor_id
            request.session.save()
            # print(response.status_code)

            if response.status_code == 200:
                # return HttpResponse(f"Data successfully stored in the Database. API response: {response.text}")
                # return render(request,"Doctor/clinic.html",{"doctor_id":doctor_id})
                return redirect(addClinic)
            else:
                return HttpResponse(f"Failed to store data in the Database. API response: {response.text}")




def addClinic(request):
    if(request.method=='GET'):
        # request.session['location_id'] =5
        # location_id=request.session['location_id']
        # doctor_id=request.session['doctor_id']
        # print(location_id)
        if 'location_id' in request.session:
            location_id=request.session['location_id']
            print(location_id)
            api_data={"doctor_location_id":location_id}
            # api_url="http://127.0.0.1:8000/api/get_all_doctor_location/"
            api_url="http://13.233.211.102/doctor/api/get_all_doctor_location/"
            response=requests.post(api_url,json=api_data)
            data=response.json().get("message_data",{})
            # print(data)
            return render(request,"Doctor/clinicaddandupdate.html",{"data":data[0],'location_id':location_id})
        else:
            request.session['location_id']=None
            return render(request,"Doctor/clinicaddandupdate.html",{"location_id":None})
    
    else:
        clinicname=request.POST['clinicName']
        pincode=request.POST["pincode"]
        city=request.POST["city"]
        state=request.POST["state"]
        country=request.POST["country"]
        address=request.POST["address"]
        latitude=request.POST['latitude']
        longitude=request.POST['longitude']
        location_id=request.session['location_id']
        
        api_data={
                "location_title":clinicname,
                "location_type": 1,  #for now bydefault 1 means clinic
                "location_address": address,
                "location_latitute": latitude,
                "location_longitute": longitude,
                "location_city_id": 1,
                "location_state_id": 1,
                "location_country_id": 1,
                "location_pincode":pincode,
                "location_status": 1,  #bydefault 1 means active
                "isdeleted":0 #bydefault put 0 later update the api.
            }
        
        if location_id is not None :
            api_data['doctor_location_id']=location_id
            # api_url="http://127.0.0.1:8000/api/update_doctor_location/"
            api_url="http://13.233.211.102/doctor/api/update_doctor_location/"
            response=requests.post(api_url,json=api_data)
            messages.success(request, 'Clinic Details updated successfully!')
            return redirect(settingdashboard)
        
        else:
            api_data['doctor_id']=request.session['doctor_id']
            print(api_data['doctor_id'])
            # api_url = "http://127.0.0.1:8000/api/insert_doctor_location/"
            api_url = "http://13.233.211.102/doctor/api/insert_doctor_location/"

            response = requests.post(api_url, data=api_data)
            api_response = response.json()

            # Extract location id from the response
            location_id = api_response.get("message_data", {}).get("doctor_location_id")
            request.session['location_id'] =location_id
            request.session.save()

            if response.status_code == 200:
                # return HttpResponse(f"Data successfully stored in the Database. API response: {response.text}")
                # return render(request,"Doctor/Clinic.html",{"doctor_id":doctor_id})
                return redirect(addSlot)
            else:
                return HttpResponse(f"Failed to store data in the Database. API response: {response.text}")


def addSlot(request):
    if(request.method=='GET'):
        # request.session['avalibility_id']=71
        # avalibility_id=request.session['avalibility_id']
        data={}
        if 'avalibility_id' in request.session:
            avalibility_id=request.session['avalibility_id']-20
            for i in range(1,22):
                # api_url = "http://127.0.0.1:8000/api/get_all_doctor_location_availability/"
                api_url = "http://13.233.211.102/doctor/api/get_all_doctor_location_availability/"
                api_data={"Doctor_Location_Availability_Id":avalibility_id}
                response = requests.post(api_url, json=api_data)
                avalibility_id+=1
                # details=response.json().get("message_data",{})
                data[i]=response.json().get("message_data",{})
            # print(data)
            # print(avalibility_id)
            return render(request, 'Doctor/slotsaddandupdate.html',{"data":data,'avalibility_id':avalibility_id})
        else:
            request.session['avalibility_id']=None
            return render(request,"Doctor/slotsaddandupdate.html",{"avalibility_id":None})
    
    else:
        avalibility_id=request.session['avalibility_id']
        print(avalibility_id)
        if avalibility_id is not None :
            avalibility_id=int(avalibility_id)-20
            try:    
                for day in range(1, 8):
                    for order in range(1, 4):
                        field_name_start = f'{day_name_to_string(day)}{order_to_string(order)}Start'
                        field_name_end = f'{day_name_to_string(day)}{order_to_string(order)}End'
                        
                        start_time = request.POST.get(field_name_start, '')
                        end_time = request.POST.get(field_name_end, '')
                        
                        api_data = {
                            "Doctor_Location_Availability_Id": avalibility_id,
                            "availability_day": day,
                            "availability_starttime": start_time,
                            "availability_endtime": end_time,
                            "availability_status": 1,
                            "availability_order": order
                        }
                    
                        # api_url = "http://127.0.0.1:8000/api/update_doctor_location_availability/"
                        api_url = "http://13.233.211.102/doctor/api/update_doctor_location_availability/"
                        avalibility_id+=1
                        response = requests.post(api_url, json=api_data)
                        response.raise_for_status()  # Raise exception for bad responses
                        api_url=''
                #print(avalibility_id)
                messages.success(request, 'Availibility details updated successfully!')
                return redirect(settingdashboard)

            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")
        
        else:
            try:
                doctor_id = request.session['doctor_id']
                location_id = request.session['location_id']
                
                for day in range(1, 8):
                    for order in range(1, 4):
                        field_name_start = f'{day_name_to_string(day)}{order_to_string(order)}Start'
                        field_name_end = f'{day_name_to_string(day)}{order_to_string(order)}End'
                        
                        start_time = request.POST.get(field_name_start, '')
                        end_time = request.POST.get(field_name_end, '')
                        
                        api_data = {
                            "doctor_id": doctor_id,
                            "doctor_location_id": location_id,
                            "availability_day": day,
                            "availability_starttime": start_time,
                            "availability_endtime": end_time,
                            "availability_status": 1,
                            "availability_order": order
                        }
                    
                        # api_url = "http://127.0.0.1:8000/api/insert_doctor_location_availability/"
                        api_url = "http://13.233.211.102/doctor/api/insert_doctor_location_availability/"
                        response = requests.post(api_url, json=api_data)
                        response.raise_for_status()  # Raise exception for bad responses
                api_response = response.json()
                avalibility_id = api_response.get("message_data", {}).get("doctor_location_availability_id")
                print(avalibility_id)
                request.session['avalibility_id'] =avalibility_id
                request.session.save()
                return redirect(consultaion_fee)

            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}")


def day_name_to_string(day):
    # You might need a function to convert day number to day name
    # You can customize this based on your actual requirements
    return {
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday',
    }[day]

def order_to_string(order):
    # You might need a function to convert order number to a string
    # You can customize this based on your actual requirements
    return {
        1: 'Morning',
        2: 'Afternoon',
        3: 'Evening',
    }[order]



def consultaion_fee(request):
    if(request.method=='GET'):
        # del request.session['consult_id']
        # del request.session['medic_id']
        consult_data={}
        medic_data={}
        if 'consult_id' in request.session and 'medic_id' in request.session:
            consult_id=request.session['consult_id']-2
            medic_id=request.session['medic_id']-2
            for i in range(1,4):
                api_consultdata={"consultation_fee_id":consult_id}
                # consult_url="http://127.0.0.1:8000/api/get_consultation_fee_details/"
                consult_url="http://13.233.211.102/doctor/api/get_consultation_fee_details/"
                response=requests.post(consult_url,json=api_consultdata)
                consult_data[i]=response.json().get("message_data",{})
                api_medicdata={"medical_service_fee_id":medic_id}
                # medic_url="http://127.0.0.1:8000/api/get_medical_service_fee_details/"
                medic_url="http://13.233.211.102/doctor/api/get_medical_service_fee_details/"
                response=requests.post(medic_url,json=api_medicdata)
                medic_data[i]=response.json().get("message_data",{})
                consult_id+=1
                medic_id+=1
            return render(request,"Doctor/consultMedicaddandupdate.html",{"consult_data":consult_data,"medic_data":medic_data,'consult_id':consult_id-4})
        else:
            request.session['consult_id']=None
            request.session['medic_id']=None
            return render(request,"Doctor/consultMedicaddandupdate.html",{"consult_id":None})
    
    else:
        homefv=request.POST['homeFirstVisitFee']
        homesv=request.POST['homeSecondVisitFee']
        clinicfv=request.POST['clinicFirstVisitFee']
        clinicsv=request.POST['clinicSecondVisitFee']
        phonefv=request.POST['phoneFirstVisitFee']
        phonesv=request.POST['phoneSecondVisitFee']
        daycarefee=request.POST['daycare']
        Ivfee=request.POST['IV']
        injectionfee=request.POST['injection']
        consult_id=request.session['consult_id']
        medic_id=request.session['medic_id']
        map_data={1:[homefv,homesv,daycarefee],2:[clinicfv,clinicsv,Ivfee],3:[phonefv,phonesv,injectionfee]}
        print(consult_id)
        if consult_id is not None :
            consult_id-=2
            medic_id-=2
            for i in range(1,4):
                api_consultdata={
                        "consultation_fee_id":consult_id,
                        "first_visit_fee":map_data[i][0],
                        "second_visit_fee":map_data[i][1]
                    }
                # consult_url = "http://127.0.0.1:8000/api/update_consultation_fee_details/"
                consult_url = "http://13.233.211.102/doctor/api/update_consultation_fee_details/"
                consult_response = requests.post(consult_url, json=api_consultdata)
                api_medicdata={
                        "medical_service_fee_id":medic_id,
                        "charges": map_data[i][2]
                    }
                # medic_url = "http://127.0.0.1:8000/api/update_medical_service_fee_details/"
                medic_url = "http://13.233.211.102/doctor/api/update_medical_service_fee_details/"
                medic_response = requests.post(medic_url, json=api_medicdata)
                consult_id+=1
                medic_id+=1

            print(consult_id)
            print(medic_id)
            messages.success(request, 'Consultation fee details updated successfully!')
            return redirect(settingdashboard)
        
        else:
            doctor_id = request.session['doctor_id']
            location_id = request.session['location_id']
            for i in range(1,4):
                api_data={
                    "doctor_id":doctor_id,
                    "location_id":location_id,
                    "consultation_fee": {
                        "mode_type":i,
                        "first_visit_fee":map_data[i][0] ,
                        "second_visit_fee":map_data[i][1]
                    },
                    "medical_services_fee": {
                        "service": i,
                        "charges": map_data[i][2]
                    }
                    }
                # api_url = "http://127.0.0.1:8000/api/insert_consultAndMedic_fees/"
                api_url = "http://13.233.211.102/doctor/api/insert_consultAndMedic_fees/"
                response = requests.post(api_url, json=api_data)

            api_response = response.json()
            request.session['consult_id'] = api_response.get("message_data", {}).get("consultation_fee_id")
            request.session['medic_id'] = api_response.get("message_data", {}).get("medical_service_fee_id")
            request.session.save()
            print(request.session['consult_id'],request.session['medic_id'])
            return redirect(pdf_view)
        

def pdf_view(request):
   if(request.method=="GET"):
    return render(request, 'Doctor/pdf_view.html')
   
   else:
       return redirect(dashboard)


def dashboard(request):
    return render(request,"Doctor/dashboard.html")

def no_service(request):
    return render(request, 'Doctor/no_service.html')


def settingdashboard(request):
    return render(request,"Doctor/Settingdashboard.html")


##############################################################################

# from datetime import datetime

def leaves(request):
    if(request.method=="GET"):
        api_data={"doctor_id":request.session['doctor_id']}
        # api_url = "http://127.0.0.1:8000/api/get_doctor_leave_details/"
        api_url = "http://13.233.211.102/doctor/api/get_doctor_leave_details/"
        response = requests.post(api_url, json=api_data)
        leaves=response.json().get("message_data",{})
        # print(leaves)
        data=[]
        detail={}
        for i in leaves:
            i['day']=(day_name_to_string(i['day'])).title()
            if(i['order'] in detail):
                d=detail.copy()
                data.append(d)
                detail.clear()
                detail[i['order']]=i
            else:
                detail[i['order']]=i

        data.append(detail)
        # print(data)
        global leave_data
        leave_data=data.copy()
        return render(request,"Doctor/leaves.html",{'leaves':data})
        #return HttpResponse("ok")

def leavesystem(request):
    if(request.method=="GET"):
        return render(request,"Doctor/leavesystem.html")
    else:
        doctor_id=request.session['doctor_id']
        location_id=request.session['location_id']
        data={}
        # day = day_name_to_int(request.POST.get('Day'))
        leavedate=request.POST.get("leaveDate")
        todate=request.POST.get("toDate")
        if not todate:
           todate = leavedate
        # print(todate)
        dates_between = get_dates_between(leavedate, todate)
        #print(dates_between)
        for ldate in dates_between:
            selected_date = datetime.datetime.strptime(ldate, '%Y-%m-%d')
            day_of_week = selected_date.strftime('%A')
            day = day_name_to_int(day_of_week)
            # print(day)
            for order in range(1, 4):
                    field_name_start = f'{order_to_string(order)}Start'
                    field_name_end = f'{order_to_string(order)}End'     
                    start_time = request.POST.get(field_name_start, '')
                    end_time = request.POST.get(field_name_end, '')
                    api_data = {
                                    "doctor_id": doctor_id,
                                    "location_id":location_id,
                                    "day": day,
                                    "leave_date": ldate,
                                    "order": order,
                                    "start_time":start_time,
                                    "end_time":end_time
                                }
                        
                    # api_url = "http://127.0.0.1:8000/api/insert_doctor_leave/"
                    api_url = "http://13.233.211.102/doctor/api/insert_doctor_leave/"
                    response = requests.post(api_url, json=api_data)    
               
        return redirect(leaves)
    
def updateleave(request,leave_date):
    if(request.method=='GET'):
        for leave in leave_data:
            if(leave_date == leave[1]['leave_date']):
                # print(leave)
                return render(request,"Doctor/updateleave.html",{'leave':leave})
        else:
            return HttpResponse("no")
    
    else:
        leavedate=request.POST.get("leaveDate")
        for order in range(1, 4):
                field_name_start = f'{order_to_string(order)}Start'
                field_name_end = f'{order_to_string(order)}End'     
                start_time = request.POST.get(field_name_start, '')
                end_time = request.POST.get(field_name_end, '')
                api_data = {
                                "leave_date": leavedate,
                                "order": order,
                                "start_time":start_time,
                                "end_time":end_time
                            }
                    
                # api_url = "http://127.0.0.1:8000/api/update_doctor_leave/"
                api_url = "http://13.233.211.102/doctor/api/update_doctor_leave/"
                response = requests.post(api_url, json=api_data)
                # data[order]=[start_time,end_time]
        print(response.text)
        return redirect(leaves)

def day_name_to_int(day):
    # You might need a function to convert day number to day name
    # You can customize this based on your actual requirements
    return {
        'Monday':1,
        'Tuesday':2,
        'Wednesday':3,
        'Thursday':4,
        'Friday':5,
        'Saturday':6,
        'Sunday':7,
    }[day]


     
from django.http import JsonResponse

@csrf_protect
def fetch_timings(request):
    if request.method == 'POST':
        # Get the selected date from the POST data
        selected_date = request.POST.get('selectedDate', None)
        print(selected_date)

        # Convert the selected date string to a datetime object
        selected_date = datetime.datetime.strptime(selected_date, '%Y-%m-%d')

        # Get the day from the datetime object
        day_of_week = selected_date.strftime('%A')
        # print(day_name_to_int(day_of_week))
        # print(day_of_week)

        # api_url = "http://127.0.0.1:8000/api/get_doctor_location_availability/"
        api_url = "http://13.233.211.102/doctor/api/get_doctor_location_availability/"
        api_data = {
            "doctor_id": request.session['doctor_id'],
            "availability_day": day_name_to_int(day_of_week)
        }

        response = requests.post(api_url, json=api_data)
        api_response = response.json()
        data = api_response.get("message_data", [])
        required_data={}
        for d in data:
            required_data[d['availability_order']]=[d['availability_starttime'],d['availability_endtime']]
        # print(required_data)

        # Convert data to JSON
        json_data = []

        json_entry = {
                'day': day_of_week,  # Assuming you want to display the day name for each entry
                'morning_start': required_data[1][0],
                'morning_end': required_data[1][1],
                'afternoon_start': required_data[2][0],
                'afternoon_end': required_data[2][1],
                'evening_start': required_data[3][0],
                'evening_end': required_data[3][1],
            }
        json_data.append(json_entry)

        return JsonResponse({'timings': json_data}, safe=False)


def get_dates_between(from_date_str, to_date_str):
    # Convert strings to datetime objects
    from_date = datetime.datetime.strptime(from_date_str, '%Y-%m-%d')
    to_date = datetime.datetime.strptime(to_date_str, '%Y-%m-%d')

    # Calculate the difference
    date_difference = to_date - from_date

    # Extract days from the difference
    days_difference = date_difference.days

    # Generate a list of dates between the two given dates
    date_list = [from_date + timedelta(days=i) for i in range(days_difference + 1)]

    # Convert dates back to string format
    date_strings = [date.strftime('%Y-%m-%d') for date in date_list]

    return date_strings



#################################New methods Merged##############################

def insert_medicine(request):
    if(request.method=="GET"):
        return render(request,"Doctor/add_medicine.html")
    
    else:
        insert_medicine_details = {
                # "doctor_id": request.POST["Doctor_id"],
                "doctor_id": request.session['doctor_id'],
                "medicine_code": request.POST["Medicine_Code"] ,
                "medicine_name":  request.POST["Medicine_Name"],
                "medicine_form":  request.POST["Medicine_form"],
                "medicine_frequency": request.POST["Medicine_Frequency"],
                "medicine_duration": request.POST["Medicine_Duration"],
                "medicine_dosages": request.POST["Medicine_Dosages"],
                "medicine_manufacture": request.POST["Medicine_Manufacture"],
                "medicine_packsize": request.POST["Medicine_Packsize"],
                "medicine_preservation": request.POST["Medicine_Preservation"],
                "medicine_minstock": request.POST["Medicine_Minstock"],
                "medicine_gst": request.POST["Medicine_GST"],
                "medicine_content_name": request.POST["Medicine_Content_name"],
                }
        api_url = "http://13.233.211.102/doctor/api/insert_doctor_medicine/"
        response = requests.post(api_url,json=insert_medicine_details)
        print(response.text)

        if response.status_code == 200:
            messages.success(request, 'Medicine details Added successfully!')
            return redirect(get_all_medicines)
        else:
            return HttpResponse("medicine data is not submitted")

def update_medicine(request,doctor_medicine_id):
    if(request.method=="GET"):
        for medicine in all_medicines:
            if(doctor_medicine_id==medicine['doctor_medicine_id']):
                # print(medicine)
                return render(request,'Doctor/add_medicine.html',{'medicine':medicine})
        else:
            return HttpResponse("no data found")
    else:
        update_medicine_details = { 
                "medicine_code": request.POST["Medicine_Code"] ,
                "medicine_name":  request.POST["Medicine_Name"],
                "medicine_form":  request.POST["Medicine_form"],
                "medicine_frequency": request.POST["Medicine_Frequency"],
                "medicine_duration": request.POST["Medicine_Duration"],
                "medicine_dosages": request.POST["Medicine_Dosages"],
                "medicine_manufacture": request.POST["Medicine_Manufacture"],
                "medicine_packsize": request.POST["Medicine_Packsize"],
                "medicine_preservation": request.POST["Medicine_Preservation"],
                "medicine_minstock": request.POST["Medicine_Minstock"],
                "medicine_gst": request.POST["Medicine_GST"],
                "medicine_content_name": request.POST["Medicine_Content_name"],
                }
        api_url = f'http://13.233.211.102/doctor/api/update_doctor_medicine/{doctor_medicine_id}/'
        response = requests.post(api_url,json=update_medicine_details)

        if response.status_code == 200:
            messages.success(request, 'Medicine details Updated successfully!')
            return redirect(get_all_medicines)
        else:
            return HttpResponse("medicine data not updated..")


def get_all_medicines(request):
    api_data = {"doctor_id":request.session['doctor_id']}
    api_url = 'http://13.233.211.102/doctor/api/get_all_doctor_medicine_bydoctorid_medicinename/'

    response = requests.post(api_url,json=api_data)
    global all_medicines
    all_medicines=response.json().get('message_data', {})
    # for i in all_medicines:
    #     print(i)
    #     print('----------------------------------------------------------')
    # return HttpResponse(all_medicines)
    return render(request,'Doctor/get_all_medicine.html',{'all_medicines':all_medicines})


def delete_medicine(request,doctor_medicine_id):
    if doctor_medicine_id:
        api_url = f'http://13.233.211.102/doctor/api/delete_doctor_medicine/{doctor_medicine_id}/'
        response = requests.delete(api_url)
        if response.status_code == 200:
            messages.success(request, 'Medicine details Deleted successfully!')
            return redirect(get_all_medicines)
                    
        else:
            return HttpResponse("Data is not Deleted........")
    else:
        return  HttpResponse("Id is Invalid......")



############################Lab Report##########################
    
def add_lab_report(request):
    if(request.method=='GET'):
        return render(request,"Doctor/addandupdate_labreport.html")
    
    else:
        api_data = {
        "doctor_id":request.session['doctor_id'],
        "investigation_category":request.POST['investigation_category'],
        "investigation_name":request.POST["investigation_name"]
        }
        api_url= f"http://13.233.211.102/doctor/api/insert_labinvestigations/"
        response = requests.post(api_url,json=api_data)
        print(response.text)
        messages.success(request, 'Lab report Added successfully!')
        return redirect(get_all_lab_report)


def get_all_lab_report(request):
    doctor_id ={"doctor_id":request.session['doctor_id']}
    api_url ='http://13.233.211.102/medicalrecord/api/get_labinvestigation_bydoctorid/'

    response = requests.post(api_url,json=doctor_id)
    #print("lab_investigation_report_data:", lab_investigation_report_data)
    global lab_investigation_report
    lab_investigation_report =response.json().get('message_data')
    # print(lab_investigation_report)
    return render(request,'Doctor/lab_report.html',{'lab_reports':lab_investigation_report})


# def update_lab_report(request,investigation_id):
#     if(request.method=="GET"):
#         for report in lab_investigation_report:
#             if(investigation_id==report['investigation_id']):
#                 # print(medicine)
#                 return render(request,'Doctor/addandupdate_labreport.html',{'report':report})
#         else:
#             return HttpResponse("no data found")
#     else:
#         api_data = { 
#                   "doctor_id":request.session['doctor_id'],
#                   "investigation_id":investigation_id,
#                   "investigation_category":request.POST['investigation_category'],
#                   "investigation_name":request.POST["investigation_name"]
#                 }
#         api_url = f"http://13.233.211.102/doctor/api/update_labinvestigations/"
#         response = requests.post(api_url,json=api_data)
#         print(response.text)
#         if response.status_code == 200:
#             messages.success(request, 'Lab report Updated successfully!')
#             return redirect(get_all_lab_report)
#         else:
#             return HttpResponse("lab data is not updated.")

def update_lab_report(request,investigation_id):
    if(request.method=="GET"):
        doctor_id ={"doctor_id":request.session['doctor_id']}
        api_url ='http://13.233.211.102/medicalrecord/api/get_labinvestigation_bydoctorid/'

        response = requests.post(api_url,json=doctor_id)
        #print("lab_investigation_report_data:", lab_investigation_report_data)
        global lab_investigation_report
        lab_investigation_report =response.json().get('message_data')
        for report in lab_investigation_report:
            if(investigation_id==report['investigation_id']):
                # print(medicine)
                return render(request,'Doctor/addandupdate_labreport.html',{'report':report})
        else:
            return HttpResponse("no data found")
    else:
        api_data = { 
                  "doctor_id":request.session['doctor_id'],
                  "investigation_id":investigation_id,
                  "investigation_category":request.POST['investigation_category'],
                  "investigation_name":request.POST["investigation_name"]
                }
        api_url = f"http://13.233.211.102/doctor/api/update_labinvestigations/"
        response = requests.post(api_url,json=api_data)
        print(response.text)
        if response.status_code == 200:
            messages.success(request, 'Lab report Updated successfully!')
            return redirect(get_all_lab_report)
        else:
            return HttpResponse("lab data is not updated.")


def delete_lab_report(request,investigation_id):
    if investigation_id:
        api_url = f'http://13.233.211.102/doctor/api/delete_labinvestigations/'
        api_data={'investigation_id':investigation_id}
        response = requests.post(api_url,api_data)
        if response.status_code == 200:
            messages.success(request, 'Lab Report Deleted successfully!')
            return redirect(get_all_lab_report)
                    
        else:
            return HttpResponse("Data is not Deleted........")
    else:
        return  HttpResponse("Id is Invalid......")
    


#####################Appointments##############################

def get_all_doctor_appointments(request):
    return render(request,'Doctor/appointments.html')


@csrf_protect
def fetch_data(request):
    if request.method == 'POST':
        # Get the selected date from the POST data
        selected_date = request.POST.get('selectedDate', None)
        print(selected_date)

        api_url = "http://13.233.211.102/appointment/api/get_doctor_appointments/"
        api_data ={
            "Doctor_Id":request.session['doctor_id'],
            "Appointment_DateTime": selected_date+" 00:00:00"
        }

        response = requests.get(api_url, json=api_data)
        # print(response.text)
        api_response = response.json()
        data = api_response.get("message_data", [])
        print(data)

        return JsonResponse(data, safe=False) 
    
    return HttpResponse('hi')


####################################Appointment and Consultation################
def initial_assesment(request,appointment_id):
    if(request.method=="GET"):
        request.session['appointment_id']=appointment_id
        print(request.session['appointment_id'])
        api_data = {"appointment_id": appointment_id}
        # api_url = 'http://127.0.0.1:8000/api/get_patient_by_appointment_id/'
        api_url ='http://13.233.211.102/appointment/api/get_patient_by_appointment_id/'
        response = requests.post(api_url, json=api_data)

        # request.session['appointment_id'] = api_data
        # print("api",api_data)
        if response.status_code == 200:
            data = response.json().get('message_data')
            data1=data.get('appointment details', {})
            request.session['appointment_details']=data1
            print(data1)
        
        # vital_url="http://localhost:8000/api/get_patientvitals_by_appointment_id/"
        vital_url="http://13.233.211.102/medicalrecord/api/get_patientvitals_by_appointment_id/"
        vital_response=requests.post(vital_url,json={"appointment_id": appointment_id})
        # print(vital_response.text)
        vital_data=vital_response.json().get('message_data')
        if(vital_response.json().get('message_code')==1000):
            # print("vitals_data: ",vital_data)
            return render(request, 'Doctor/initial_assesment.html',{"data1":data1,"vital_data":vital_data})
        else:
            return render(request, 'Doctor/initial_assesment.html',{"data1":data1})



    else:
        print(request.POST['phoneno'])
        # patient_url="http://localhost:8000/api/get_patient_details_by_phone/"
        patient_url="http://13.233.211.102/pateint/api/get_patient_details_by_phone/"
        api_data={"phone_number":request.POST['phoneno']}
        patient_response=requests.post(patient_url,api_data)
        print(patient_response.text)
        if(patient_response.json().get('message_code')==1000):
            patient_data=patient_response.json().get("message_data")
            print(patient_data)
            patient_id=patient_data['patient_id']
            print("if pateint_id",patient_id)
        else:
            appointment_details=request.session['appointment_details']
            print(appointment_details)
            fullname=(appointment_details['appointment_name']).split(" ")
            print(fullname)
            
            # patient_url="http://localhost:8000/api/insert_patient/"
            patient_url="http://13.233.211.102/pateint/api/insert_patient/"
            patient_apidata={
                "patient_mobileno": appointment_details['appointment_mobileno'],
                "patient_firstname": fullname[0],
                "patient_lastname": fullname[1],
                # "patient_fateherhusbandname": "vijay",
                "patient_gender":appointment_details['appointment_gender'],
                "patient_dateofbirth": "2023-12-15",
                "patient_maritalstatus": 1,
                "patient_aadharnumber": "1234567890123456",
                "patient_universalhealthid": 123456,
                "patient_bloodgroup": 1,
                "patient_emergencycontact": "9876543210",
                "patient_address": "123 Main Street",
                "patient_cityid": 1,
                "patient_stateid": 1,
                "patient_countryid": 1
            }
            patientdata_response=requests.post(patient_url,json=patient_apidata)
            print(patientdata_response.text)
            patient_id=((patientdata_response.json().get("message_data"))[0]).get("Patient_Id")
            print("else patient_id",patient_id)

        patient_data = {
            "patient_id":patient_id,
            "doctor_id": request.session['doctor_id'],
            "operator_id": 1,
            "patient_status":1, #bydefault 1=OPD
            "patient_heartratepluse": request.POST['heart_rate'],
            "patient_bpsystolic": request.POST['bp_s'],
            "patient_bpdistolic": request.POST['bp_d'],
            "patient_painscale": request.POST['pain_scale'],
            "patient_respiratoryrate": request.POST['respiratory_rate'],
            "patient_temparature": request.POST['temp'],
            "patient_chest": request.POST['chest'],
            "patient_ecg": request.POST['ecg'],
            "weight":request.POST['weight'],
            "height":request.POST['height'],
            "bmi":request.POST['bmi'],
            "appointment_id":appointment_id,
            # "consultation_id":0    
        }
        # api_url = 'http://127.0.0.1:8000/api/insert_patients_vitals/'
        api_url ='http://13.233.211.102/medicalrecord/api/insert_patients_vitals/'
        response = requests.post(api_url, json=patient_data)
        print(response.text)

        vitals_id = response.json().get('message_data', {})  # Getting 'message_data' safely
        vitals_id = (vitals_id[0]).get("Patient_Biometricid")
        request.session['vitals_id']=vitals_id
        print(vitals_id)
        print("vitals_id",vitals_id)

        update_status_url="http://13.233.211.102/appointment/api/update_appointment_status"
        status_response=requests.post(update_status_url,json={"appointment_id":appointment_id,"appointment_status":2})
        print(status_response.text)
        
        # return render(request, 'initial_assesment.html',{"data":data.get('appointment details', {}),"vitals_id":vitals_id,"data1":data1})
        # return redirect(consultation)
        return redirect(consultation)

def update_initial_assesment(request):
    appointment_id=request.POST['appointment_id']
    request.session['appointment_id']=appointment_id
    api_data = {
            # "patient_id":request.POST['patient_id'],
            # "patient_id":1,
            # "doctor_id": request.POST['doctor_id'],
            # "operator_id": request.POST['doctor_id'],
            # "patient_status": request.POST['patient_status'],
            "patient_heartratepluse": request.POST['heart_rate'],
            "patient_bpsystolic": request.POST['bp_s'],
            "patient_bpdistolic": request.POST['bp_d'],
            "patient_painscale": request.POST['pain_scale'],
            "patient_respiratoryrate": request.POST['respiratory_rate'],
            "patient_temparature": request.POST['temp'],
            "patient_chest": request.POST['chest'],
            "patient_ecg": request.POST['ecg'],
            "weight":request.POST['weight'],
            "height":request.POST['height'],
            "bmi":request.POST['bmi'],
            "appointment_id":appointment_id,
            
        }
    # url="http://localhost:8000/api/update_patientvitals_by_appointment_id/"
    url="http://13.233.211.102/medicalrecord/api/update_patientvitals_by_appointment_id/"
    response=requests.post(url,json=api_data)
    print(response.text)
    vdata=response.json().get('message_data')
    request.session['vitals_id']= vdata['patient_biometricid']
    return  redirect(consultation)


# ####################################Consultation###########################
def consultation(request):
    if(request.method == "GET"):
        appointment_id= request.session['appointment_id']
        #appointment_id=1
        print("appointment_id",appointment_id)
        
        All_medicines(requests,request.session['doctor_id'])
############################################# KCO for for fetch the values########################
        KCO(requests)
        
    
############################################# ADVICE for for fetch the values########################
        ADVICE(requests)
                     
#################################################################################################################    
        get_labinvestigation(requests,request.session['doctor_id'])   # function call get_labinvestigation
#######################################################################################################        
        get_instruction(requests)  # function call get_labinvestigatio

 ################################################################################################################       
       
        Get_Patient_By_Appointment_Id(requests,appointment_id)
#######################################################################################################################
         
        Get_Patient_Boimterics_Vitals(requests,request.session['vitals_id'])

        return render(request, 'Doctor/consultation.html', {"get_patient_by_appointment_id":get_patient_by_appointment_id,
                "get_patient_boimterics_vitals":get_patient_boimterics_vitals,"all_medicines":all_medicines,
                "kco":kco,"advice":advice,"lab_investigation_report":lab_investigation_report,
                "medicine_instruction":medicine_instruction,
               })
    else:          
########################## insert consultaions ########################################
            patient_id=(get_patient_boimterics_vitals[0]).get("patient_id")
            patient_status=(get_patient_boimterics_vitals[0]).get("patient_status")
            print("id and status",patient_id,patient_status)
            dt = request.POST["followup_datetime"]
            print(dt)
             # Parse the input datetime string into a datetime object
            datetime_obj = datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M')
            # Add 9 months to the month to get December (datetime objects are 1-indexed)
            # datetime_obj = datetime_obj.replace(month=datetime_obj.month + 9)
            # Format the datetime object as the required string format
            formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
            print("required:",formatted_datetime)
            consultation_datetime=int(request.POST["Consultation_DateTime"])
            print(consultation_datetime)
            consultation_datetime = datetime.datetime.fromtimestamp(consultation_datetime).strftime("%Y-%m-%d %H:%M:%S")

            insert_consultation = {
                "Patient_Id": patient_id,
                "Doctor_Id":request.session["doctor_id"] ,
                "Patient_Status":patient_status,
                "Consultation_DateTime":consultation_datetime,#appointment_datetime
                "Instructions":request.POST["Instructions"],
                "Fess":request.POST["Fess"],
                "referred_to_doctor":request.POST["referred_to_doctor"],
                "referred_by_doctor":request.POST["referred_by_doctor"],
                "Followup_DateTime":formatted_datetime,
                "appointment_id":request.session['appointment_id'],
            }
            consultation_api_url = 'http://13.233.211.102/medicalrecord/api/insert_consultation'

            consultation_response = requests.post(consultation_api_url, json=insert_consultation)
            print("consultation_response : ", consultation_response.text)
            consultation = consultation_response.json().get('message_data', {})
            consultation_id=consultation['consultation_id']
            print("consultation_ID : ", consultation)
            #update appointment status to 3 means completed.
            update_status_url="http://13.233.211.102/appointment/api/update_appointment_status"
            status_response=requests.post(update_status_url,json={"appointment_id":request.session['appointment_id'],"appointment_status":3})
            print(status_response.text)
            consultation_id = consultation['consultation_id']
            print(consultation_id )
            request.session[ 'consultation_id' ] = consultation_id   # Create Session for Consulation ID


# ################################ insert_patient__vitals ###############################################

            api_data = {
                "Doctor_Id":request.session["doctor_id"],
                "Patient_Id":patient_id,
                "Patient_Status":patient_status,
                "Consultation_DateTime":request.POST["Consultation_DateTime"],
                "patient_heartratepluse":request.POST["Patient_HeartRatePluse"],
                "patient_bpsystolic":request.POST["Patient_BPSystolic"],
                "patient_bpsystolic":request.POST["Patient_BPDistolic"],
                "patient_painscale":request.POST["Patient_PainScale"],
                "patient_respiratoryrate":request.POST["Patient_RespiratoryRate"],
                "patient_temparature":request.POST["Patient_Temparature"],
                "patient_chest":request.POST["Patient_Chest"],
                "patient_ecg":request.POST["Patient_ECG"],
                "weight":request.POST['weight'],
                "further_assited":"0",
                'appointment_id':request.session['appointment_id'],
                "consultation_id":consultation_id   
        }
            # url="http://localhost:8000/api/update_patientvitals_by_appointment_id/"
            url="http://13.233.211.102/medicalrecord/api/update_patientvitals_by_appointment_id/"
            response=requests.post(url,json=api_data)
            print(response.text)
            
###############################  insert finding symptoms(complaints & Diagnosis) ########################################
            all_kco=request.POST['kco']
            alladvice=request.POST['advice']
             # Splitting the strings by newline characters and removing empty strings
            kco_list = [kco.strip() for kco in all_kco.split('\n') if kco.strip()]
            advice_list = [advice.strip() for advice in alladvice.split('\n') if advice.strip()]

            # Joining the lists into single strings separated by commas
            kco_str = ', '.join(kco_list)
            advice_str = ', '.join(advice_list)

            print(kco_str)
            print(advice_str)
            finding_symptoms= {
                "patient_id":patient_id, 
                "doctor_id": request.session["doctor_id"],
                "patient_status": patient_status,
                "findgings_datetime": "2023-12-15 15:10:28", 
                "consultation_id":consultation_id,
                "findings": request.POST["Diagnosis"],
                "symtoms": request.POST['complaint_details'],
                "kco":kco_str,
                "advice":advice_str

                }
            insert_patient_findingsandsymtoms_url = "http://13.233.211.102/medicalrecord/api/insert_patient_findingsandsymtoms/"

            findingsandsymtoms_response = requests.post(insert_patient_findingsandsymtoms_url,json=finding_symptoms)
            print(findingsandsymtoms_response.text)

#################################Prescription###############################
            prescritption=request.POST['Prescription']
            print(prescritption)
            prescription_url="http://13.233.211.102/medicalrecord/api/insert_prescriptions/"
            prescription_data={
                "doctor_id": request.session["doctor_id"],
                "patient_id": patient_id,
                "patient_status": patient_status,
                "consultation_id":consultation_id,
                "prescription_datetime": "2024-02-01 12:30:00",
                "prescription_details": prescritption
            }
            prescritption_response=requests.post(prescription_url,json=prescription_data)
            print(prescritption_response.text)
            prescription_id=(prescritption_response.json().get("message_data"))[0]['Prescriptions_Id']
            print("prescroption id:",prescription_id)
            
#############################Patient Medications##############################
            mode = request.POST.get('Mode')
            medicine = request.POST.get('Medicine')
            days = request.POST.get('days')
            dosage = request.POST.get('dosage')
            language = request.POST.get('Language')
            instruction = request.POST.get('Instructions')
            print(language,instruction,mode,medicine,days,dosage) 
            instruction_list= instruction.split(",")
            mode_list=mode.split(",")
            medicine_list=medicine.split(",")
            days_list=days.split(",")
            dosage_list=dosage.split(",")
            language_list=language.split(",")
            med_id_list=[]
            for name in medicine_list:
                for medicine in all_medicines:
                    if(name==medicine['medicine_name']):
                        med_id_list.append(medicine['doctor_medicine_id'])
            if medicine_list[0]:
                # medication_url="http://127.0.0.1:8000/api/insert_patient_medications/"
                medication_url="http://13.233.211.102/medicalrecord/api/insert_patient_medications/"
                for i in range(len(medicine_list)):
                        medication_data={
                            "doctor_id": request.session["doctor_id"],
                            "patient_id": patient_id,
                            "patient_status": patient_status,
                            "consultation_id":consultation_id,
                            "prescription_id":prescription_id,
                            "medication_datetime": "2024-02-01 12:30:00",
                            "medicine_id": med_id_list[i],
                            "medicine_form": mode_list[i],
                            "medicine_name": medicine_list[i],
                            "medicine_duration":days_list[i],
                            "medicine_doses": dosage_list[i],
                            "medicine_dose_interval": "8 hours",
                            "medicine_instruction_id": instruction_list[i],
                            "medicine_Category": 7,
                            "Medicine_ExtraField1": 8,
                            "Medicine_ExtraField2": 9
                        }
                        response=requests.post(medication_url,json=medication_data)
                        print(response.text)
                print(language_list,instruction_list,mode_list,medicine_list,days_list,dosage_list,med_id_list)
            # print(all_medicines)
            #print(med_id_list)

            else:
                print("no data")
            
##############################Patient Lab Investigations###########################
            labs=request.POST['lab_tests']
            labs_list = [labs.strip() for labs in labs.split('\n') if labs.strip()]
            labinvest_id=[]
            print(labs_list)
            if(labs_list):
                # lab_url="http://localhost:8000/api/insert_patient_labinvestigations/"
                lab_url="http://13.233.211.102/medicalrecord/api/insert_patient_labinvestigations/"
                labs_data={
                "doctor_id": request.session["doctor_id"],
                "patient_id": patient_id,
                "patient_status": patient_status,
                "consultation_id": consultation_id,
                "prescription_id": prescription_id,
                "labinvestigation_datetime": "2022-02-11 14:30:00",
                # "labinvestigation_category": 2,
                "patient_labtestid": 1,#investigation_id
                "patient_labtestreport": "Sample Report",
                "patient_labtestsample": 3,
                "patient_labtestreport_check": 1,
                "lattest_extrafield1": 42,
                "isdeleted":0
            }
                for category in labs_list:
                    labs_data['labinvestigation_category']=category
                    lab_response=requests.post(lab_url,json=labs_data)
                print(lab_response.text)
            else:
                print("no labs found")
               
            return redirect(get_all_doctor_appointments)

##########################################Functions to fetch the required data for consultation Screen#######################

def Get_Patient_By_Appointment_Id(requests,appointment_id):
    # appointment_id = requests.session.get('appointment_id')
    # requests.session['appointment_id'] = id

    # print("session : ",request.session['appointment_id'])

    api_data1 = {"appointment_id": appointment_id}
    url = 'http://13.233.211.102/appointment/api/get_patient_by_appointment_id/'
    response1 = requests.post(url, json=api_data1)
    # print(response1.text)

    # data1 = {}  # Initialize data1 to an empty dictionary
    if response1.status_code == 200:
        data = response1.json()
        global get_patient_by_appointment_id 
        get_patient_by_appointment_id = data.get('message_data', {})  # Getting 'message_data' safely
        get_patient_by_appointment_id =get_patient_by_appointment_id.get('appointment details', {})
        print(get_patient_by_appointment_id)
        doctor_id = get_patient_by_appointment_id['doctor_id']
        # Create a session object
        # session = requests.session()
        # Store the doctor_id in the session
        # session['doctor_id'] = doctor_id
        # Print the doctor_id stored in the session
        # print(session['doctor_id'])
        # Print the doctor_id directly
        print("doctor_id:", doctor_id)
        print("appointments",get_patient_by_appointment_id)
                
        # Assuming the session already contains the doctor_id
        # doctor_id = session.get('doctor_id')

        # Check if doctor_id is available in the session
        if doctor_id is not None:
            print("Doctor ID:", doctor_id)
        else:
            print("Doctor ID not found in session.")

def Get_Patient_Boimterics_Vitals(requests,vitals_id):
    # id   =  request.session["biometrics_id"]
    print(id)
    
    api_data = {"patient_biometric_id": vitals_id }
    # api_url = 'http://127.0.0.1:8000/api/get_patientvitals_by_biometric_id/'
    api_url  ='http://13.233.211.102/medicalrecord/api/get_patientvitals_by_biometric_id/'
    response = requests.post(api_url, api_data)
    print(response.text)
       
    if response.status_code == 200:
        global get_patient_boimterics_vitals
        get_patient_boimterics_vitals = response.json().get('message_data', {})  # Getting 'message_data' safely
        # request.session["data2"] = data2 
        print("get_patient_boimterics_vitals :",get_patient_boimterics_vitals)
#################################################################################################################
def All_medicines(requests,doctor_id):

    all_medicine_api_data = {"doctor_id":doctor_id}
    all_medicine_url = 'http://13.233.211.102/doctor/api/get_all_doctor_medicine_bydoctorid_medicinename/'

    all_medicine_response = requests.post(all_medicine_url,json=all_medicine_api_data)
    # print(all_medicine_response.text)
    if all_medicine_response.status_code == 200:
        global all_medicines
        all_medicines = all_medicine_response.json().get('message_data', {})
        print(all_medicines)
        # doctor_medicine_id = all_medicines[0]['doctor_medicine_id']
        # print("doctor_medicine_id: ",doctor_medicine_id)
        # request.session['doctor_medicine_id'] = medicine_id 


def ADVICE(requests):
    advice_data = {"DataCodeName":"ADVICE"}
    advice_url ='http://13.233.211.102/masters/api/get_datacodemaster_byname'

    advice_response = requests.post(advice_url,json=advice_data)
        # print(kco_response.text)
    global advice
    advice = advice_response.json().get('message_data')
    print(advice)


def KCO(requests):
    kco_data = {"DataCodeName":"KCO"}
    kco_url ='http://13.233.211.102/masters/api/get_datacodemaster_byname'

    kco_response = requests.post(kco_url,json=kco_data)
    # print(kco_response.text)
    global kco
    kco = kco_response.json().get('message_data')
    print(kco)

def get_instruction(requests):
        doctor_id ={ "Doctor_Id":"1"}
        url_instruction = 'http://13.233.211.102/masters/api/get_medicine_instructionsbydoctorId'

        medicine_instruction_response = requests.post(url_instruction, json = doctor_id)
        print("medicine_instruction_response:",medicine_instruction_response.text)

        global medicine_instruction
        medicine_instruction = medicine_instruction_response.json().get('message_data', {})
        # language= medicine_instruction[1]['instruction_language']
        # instruction = medicine_instruction[2]['instruction_text']
        print("Medicine_Instructions: ",medicine_instruction)

def get_labinvestigation(requests,doctor_id):
    doctor_id ={"doctor_id":doctor_id}
    lab_investigation_url ='http://13.233.211.102/medicalrecord/api/get_labinvestigation_bydoctorid/'

    lab_investigation_report_data = requests.post(lab_investigation_url,json=doctor_id)
    #print("lab_investigation_report_data:", lab_investigation_report_data)
    global lab_investigation_report
    lab_investigation_report = lab_investigation_report_data.json().get('message_data')
    print("lab_investigation_report:", lab_investigation_report)

 
