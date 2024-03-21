# def addSlot(request):
#     if(request.method=='GET'):
#         return render(request,'Doctor/doctorAvalibility.html')
    
#     else:
#         doctor_id=request.session['doctor_id']
#         location_id=request.session['location_id']
#         for day in range(1, 8):  # 1 to 7 representing Monday to Sunday
#             for order in range(1, 4):  # 1 to 3 representing Morning, Afternoon, Evening
#                 field_name_start = f'{day_name_to_string(day)}{order_to_string(order)}Start'
#                 field_name_end = f'{day_name_to_string(day)}{order_to_string(order)}End'
#                 start_time = request.POST.get(field_name_start, '')
#                 end_time = request.POST.get(field_name_end, '')
#                 # availability_data[f'{day}-{order}'] = {'start_time': start_time, 'end_time': end_time}
#                 api_data={
#                             "doctor_id":doctor_id,
#                             "doctor_location_id":location_id,
#                             "availability_day":day,
#                             "availability_starttime":start_time,
#                             "availability_endtime":end_time,
#                             "availability_status": 1,
#                             "availability_order":order
#                         }
#                 api_url = "http://127.0.0.1:8000/api/insert_doctor_location_availability/"
#                 response = requests.post(api_url, json=api_data)
            
        
#         return HttpResponse("All Process Done")


#         # # Handle the API response as needed
#         # if response.status_code == 200:
#         #     return HttpResponse('Data successfully saved!')
#         # else:
#         #     return HttpResponse('Failed to save data. Please try again.')

#=============================================================================================

# def doctorReg(request):
#     if(request.method=="GET"):
#       return render(request,"Doctor/doctorReg.html")
        
#     else:
#         fname=request.POST['firstName']
#         lname=request.POST['lastName']
#         regno=request.POST["registrationNumber"]
#         aadharNumber=request.POST["aadharNumber"]
#         pincode=request.POST["pincode"]
#         city=request.POST["city"]
#         state=request.POST["state"]
#         country=request.POST["country"]
#         address=request.POST["address"]
#         dob=request.POST["dob"]
#         mstatus=request.POST["maritalStatus"]
#         gender=request.POST["gender"]
#         email=request.POST["email"]
#         mno=request.POST["mobileNumber"]

#         api_data={
#                 "doctor_firstname": fname,
#                 "doctor_lastname": lname,
#                 "doctor_mobileno": mno,
#                 "doctor_email":email,
#                 "doctor_dateofbirth": dob,
#                 "doctor_maritalstatus":mstatus,
#                 "doctor_gender":gender,
#                 "doctor_aadharnumber": aadharNumber,
#                 "doctor_address": address,
#                 "doctor_cityid": 1,
#                 "doctor_stateid": 1,
#                 "doctor_countryid": 1,
#                 "doctor_pincode": pincode,
#                 "doctor_registrationno": regno,
#                 "isactive": 1
#             }
        
#         # api_url = "http://127.0.0.1:8000/api/insert_doctor/"
#         api_url = "http://13.233.211.102/doctor/api/insert_doctor/"

#         response = requests.post(api_url, data=api_data)
#         api_response = response.json()

#         # Extract doctor_id from the response
#         doctor_id = api_response.get("message_data", {}).get("doctor_id")
#         request.session['doctor_id'] = doctor_id
#         # print(response.status_code)

#         if response.status_code == 200:
#             # return HttpResponse(f"Data successfully stored in the Database. API response: {response.text}")
#             # return render(request,"Doctor/clinic.html",{"doctor_id":doctor_id})
#             return redirect(addClinic)
#         else:
#             return HttpResponse(f"Failed to store data in the Database. API response: {response.text}")


# def addClinic(request):
#     if(request.method=='GET'):
#         doctor_id=request.session['doctor_id']
#         return render(request,"Doctor/clinic.html",{"doctor_id":doctor_id})
    
#     else:
#         clinicname=request.POST['clinicName']
#         pincode=request.POST["pincode"]
#         city=request.POST["city"]
#         state=request.POST["state"]
#         country=request.POST["country"]
#         address=request.POST["address"]
#         latitude=request.POST['latitude']
#         longitude=request.POST['longitude']
#         doctor_id=request.POST['doctor_id'] #this will come from hidden field from doctorreg form.
        
#         api_data={
#                 "doctor_id": doctor_id,
#                 "location_title":clinicname,
#                 "location_type": 1,  #for now bydefault 1 means clinic
#                 "location_address": address,
#                 "location_latitute": latitude,
#                 "location_longitute": longitude,
#                 "location_city_id": 1,
#                 "location_state_id": 1,
#                 "location_country_id": 1,
#                 "location_pincode":pincode,
#                 "location_status": 1,  #bydefault 1 means active
#                 "isdeleted":0 #bydefault put 0 later update the api.
#             }
        

#         # api_url = "http://127.0.0.1:8000/api/insert_doctor_location/"
#         api_url = "http://13.233.211.102/doctor/api/insert_doctor_location/"

#         response = requests.post(api_url, data=api_data)
#         api_response = response.json()

#         # Extract location id from the response
#         location_id = api_response.get("message_data", {}).get("doctor_location_id")
#         request.session['location_id'] =location_id

#         if response.status_code == 200:
#             # return HttpResponse(f"Data successfully stored in the Database. API response: {response.text}")
#             # return render(request,"Doctor/Clinic.html",{"doctor_id":doctor_id})
#             return redirect(addSlot)
#         else:
#             return HttpResponse(f"Failed to store data in the Database. API response: {response.text}")


# def addSlot(request):
#     if request.method == 'GET':
#         return render(request, 'Doctor/doctorAvalibility.html')
    
#     else:
#         try:
#             doctor_id = request.session['doctor_id']
#             location_id = request.session['location_id']
            
#             for day in range(1, 8):
#                 for order in range(1, 4):
#                     field_name_start = f'{day_name_to_string(day)}{order_to_string(order)}Start'
#                     field_name_end = f'{day_name_to_string(day)}{order_to_string(order)}End'
                    
#                     start_time = request.POST.get(field_name_start, '')
#                     end_time = request.POST.get(field_name_end, '')
                    
#                     api_data = {
#                         "doctor_id": doctor_id,
#                         "doctor_location_id": location_id,
#                         "availability_day": day,
#                         "availability_starttime": start_time,
#                         "availability_endtime": end_time,
#                         "availability_status": 1,
#                         "availability_order": order
#                     }

#                     api_url = "http://127.0.0.1:8000/api/insert_doctor_location_availability/"
#                     # api_url = "http://13.233.211.102/doctor/api/insert_doctor_location_availability/"
#                     response = requests.post(api_url, json=api_data)
#                     response.raise_for_status()  # Raise exception for bad responses

#             return redirect(consultaion_fee)

#         except Exception as e:
#             return HttpResponse(f"An error occurred: {str(e)}")


# def day_name_to_string(day):
#     # You might need a function to convert day number to day name
#     # You can customize this based on your actual requirements
#     return {
#         1: 'monday',
#         2: 'tuesday',
#         3: 'wednesday',
#         4: 'thursday',
#         5: 'friday',
#         6: 'saturday',
#         7: 'sunday',
#     }[day]

# def order_to_string(order):
#     # You might need a function to convert order number to a string
#     # You can customize this based on your actual requirements
#     return {
#         1: 'Morning',
#         2: 'Afternoon',
#         3: 'Evening',
#     }[order]

# def consultaion_fee(request):
#     if(request.method=='GET'):
#         return render(request,"Doctor/demo.html")
    
#     else:
#         doctor_id = request.session['doctor_id']
#         location_id = request.session['location_id']

#         homefv=request.POST['homeFirstVisitFee']
#         homesv=request.POST['homeSecondVisitFee']
#         clinicfv=request.POST['clinicFirstVisitFee']
#         clinicsv=request.POST['clinicSecondVisitFee']
#         phonefv=request.POST['phoneFirstVisitFee']
#         phonesv=request.POST['phoneSecondVisitFee']
#         daycarefee=request.POST['daycare']
#         Ivfee=request.POST['IV']
#         injectionfee=request.POST['injection']
#         map_data={1:[homefv,homesv,daycarefee],2:[clinicfv,clinicsv,Ivfee],3:[phonefv,phonesv,injectionfee]}

#         for i in range(1,4):
#             api_data={
#                 "doctor_id":doctor_id,
#                 "location_id":location_id,
#                 "consultation_fee": {
#                     "mode_type":i,
#                     "first_visit_fee":map_data[i][0] ,
#                     "second_visit_fee":map_data[i][1]
#                 },
#                 "medical_services_fee": {
#                     "service": i,
#                     "charges": map_data[i][2]
#                 }
#                 }
#             api_url = "http://127.0.0.1:8000/api/insert_consultAndMedic_fees/"
#             response = requests.post(api_url, json=api_data)

#         # form_data = request.POST.dict()

#         return HttpResponse("ok")
        
        
# @csrf_protect
# def fetch_timings(request):
#     if request.method == 'POST':
#         # Get the selected date from the POST data
#         selected_date = request.POST.get('selectedDate', None)
#         print(selected_date)
#         # Convert the selected date string to a datetime object
#         selected_date = datetime.strptime(selected_date, '%Y-%m-%d')

#         # Get the day from the datetime object
#         day_of_week = selected_date.strftime('%A')
#         print(day_name_to_int(day_of_week.lower()))
#         print(day_of_week)
#         api_url = "http://127.0.0.1:8000/api/get_doctor_location_availability/"
#         api_data={
#                 "doctor_id": request.session['doctor_id'],
#                 "availability_day": day_name_to_int(day_of_week.lower())
#             }
#         response = requests.post(api_url, json=api_data)
#         api_response = response.json()
#         data=api_response.get("message_data", {})
#         print(data)

#         return HttpResponse(selected_date)

         

#         #return JsonResponse({'timings': timings_list})

# def leavesystem(request):
#     if(request.method=="GET"):
#         return render(request,"Doctor/leavesystem.html")
#     else:
#         doctor_id=request.session['doctor_id']
#         location_id=request.session['location_id']
#         data={}
#         day = day_name_to_int(request.POST.get('Day'))
#         leavedate=request.POST.get("leaveDate")
#         for order in range(1, 4):
#                 field_name_start = f'{order_to_string(order)}Start'
#                 field_name_end = f'{order_to_string(order)}End'     
#                 start_time = request.POST.get(field_name_start, '')
#                 end_time = request.POST.get(field_name_end, '')
#                 api_data = {
#                                 "doctor_id": doctor_id,
#                                 "location_id":location_id,
#                                 "day": day,
#                                 "leave_date": leavedate,
#                                 "order": order,
#                                 "start_time":start_time,
#                                 "end_time":end_time
#                             }
                    
#                 api_url = "http://127.0.0.1:8000/api/insert_doctor_leave/"
#                         # api_url = "http://13.233.211.102/doctor/api/insert_doctor_location_availability/"
#                 response = requests.post(api_url, json=api_data)
#                 # data[order]=[start_time,end_time]

#         return redirect(leaves)

