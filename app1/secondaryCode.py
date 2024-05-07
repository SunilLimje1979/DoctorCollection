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



# def Consultation(request):
#     if(request.method == "GET"):
#         appointment_id= request.session['appointment_id']
#         #appointment_id=1
#         print("appointment_id",appointment_id)
#         Get_Patient_By_Appointment_Id(requests,appointment_id)
#         if(get_patient_by_appointment_id.get('consultation_id')):
#             request.session['consultation_id']=get_patient_by_appointment_id.get('consultation_id')
#             print("the consultation id is present",get_patient_by_appointment_id.get('consultation_id'))
#             consultation_url="http://13.233.211.102/medicalrecord/api/get_consultation_byconsultationid/"
#             api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#             consult_response=requests.post(consultation_url,json=api_para)
#             consult_data=(consult_response.json().get("message_data"))[0]
#             print(consult_data)
#             epoch_timestamp = consult_data.get('followup_datetime', 0)
#             # print(epoch_timestamp)
#             # formatted_date = datetime.utcfromtimestamp(epoch_timestamp).strftime('%Y-%m-%d')
#             formatted_date=datetime.datetime.fromtimestamp(epoch_timestamp).strftime( "%Y-%m-%d %H:%M:%S")   
#             print(formatted_date)
#             consult_data['followup_datetime'] = formatted_date
#             print(consult_data)

#             #################patient findingsymptoms################
#             # finding_symptoms_url="http://localhost:8000/api/get_patient_findings_symptoms_by_consultation/"
#             finding_symptoms_url="http://13.233.211.102/medicalrecord/api/get_patient_findings_symptoms_by_consultation/"
#             api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#             symptoms_response=requests.post(finding_symptoms_url,json=api_para)
#             symptoms_data=(symptoms_response.json().get("message_data"))[0]
#             print(symptoms_data)
#             #################patient Lab Invstigations################
#             # patientlab_url="http://localhost:8000/api/get_patient_labinvestigations_by_consultation_id/"
#             patientlab_url="http://13.233.211.102/medicalrecord/api/get_patient_labinvestigations_by_consultation_id/"
#             api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#             patientlab_response=requests.post(patientlab_url,json=api_para)
#             patientlab_data=(patientlab_response.json().get("message_data"))
#             lab_list=[]
#             for i in patientlab_data:
#                 print(i)
#                 lab_list.append(i['labinvestigation_category'])
#                 print("-----------------------")
#             print(lab_list)
#             #################patient Medications################
#             patientmedic_url="http://13.233.211.102/medicalrecord/api/get_patient_medications_byconsultationid/"
#             api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#             patientmedic_response=requests.post(patientmedic_url,json=api_para)
#             patientmedic_data=(patientmedic_response.json().get("message_data"))
#             medic_list=[]
#             for i in patientmedic_data:
#                 print(i)
#                 medic_list.append(i)
#                 print("-----------------------")
#             print(medic_list)

#             #################patient prescription################
#             # prescription_url="http://localhost:8000/api/get_prescription_details/"
#             prescription_url="http://13.233.211.102/medicalrecord/api/get_prescription_details/"
#             api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#             prescription_response=requests.post(prescription_url,json=api_para)
#             print(prescription_response.text)
#             prescription_data=(prescription_response.json().get("message_data"))[0]
#             print(prescription_data)
#             #return HttpResponse("Update consultation details")
#         else:
#            symptoms_data=0
#            consult_data=0
#            lab_list=[]
#            medic_list=[]
#            prescription_data={"prescription_details":0}
#            if('consultation_id' in request.session):
#               del request.session['consultation_id']
#            print("not present",get_patient_by_appointment_id.get('consultation_id'))
        
#         All_medicines(requests,request.session['doctor_id'])
#     ############################################# KCO for for fetch the values########################
#         KCO(requests)
            
        
#     ############################################# ADVICE for for fetch the values########################
#         ADVICE(requests)
                        
#     #################################################################################################################    
#         get_labinvestigation(requests,request.session['doctor_id'])   # function call get_labinvestigation
#     #######################################################################################################        
#         get_instruction(requests)  # function call get_labinvestigatio

#     ################################################################################################################       
        
#             # Get_Patient_By_Appointment_Id(requests,appointment_id)
#     #######################################################################################################################
            
#         Get_Patient_Boimterics_Vitals(requests,request.session['vitals_id'])

#         return render(request, 'Doctor/consultation.html', {"get_patient_by_appointment_id":get_patient_by_appointment_id,
#                     "get_patient_boimterics_vitals":get_patient_boimterics_vitals,"all_medicines":all_medicines,
#                     "kco":kco,"advice":advice,"lab_investigation_report":lab_investigation_report,
#                     "medicine_instruction":medicine_instruction,'consult_data':consult_data,'symptoms_data':symptoms_data,
#                     'lab_list':lab_list,'medic_list':medic_list,'prescription':prescription_data['prescription_details'],
#                 })
#     else:          
# ########################## insert consultaions ########################################
#             patient_id=(get_patient_boimterics_vitals[0]).get("patient_id")
#             patient_status=(get_patient_boimterics_vitals[0]).get("patient_status")
#             print("id and status",patient_id,patient_status)
#             dt = request.POST["followup_datetime"]
#             print(dt)
#              # Parse the input datetime string into a datetime object
#             datetime_obj = datetime.datetime.strptime(dt, '%Y-%m-%dT%H:%M')
#             # Add 9 months to the month to get December (datetime objects are 1-indexed)
#             # datetime_obj = datetime_obj.replace(month=datetime_obj.month + 9)
#             # Format the datetime object as the required string format
#             formatted_datetime = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
#             print("required:",formatted_datetime)
#             consultation_datetime=int(request.POST["Consultation_DateTime"])
#             print(consultation_datetime)
#             consultation_datetime = datetime.datetime.fromtimestamp(consultation_datetime).strftime("%Y-%m-%d %H:%M:%S")
#             current_datetime = datetime.datetime.now()

#             # Convert to epoch time (Unix timestamp)
#             current_epoch_time = int(current_datetime.timestamp())
#             print(current_epoch_time)

#             if('consultation_id' in request.session):
#                 update_consultation = {
#                     'consultation_id':request.session['consultation_id'],
#                     "patient_id": patient_id,
#                     "doctor_id":request.session["doctor_id"] ,
#                     "patient_status":patient_status,
#                     #"consultation_datetime":consultation_datetime,#appointment_datetime
#                     "instructions":request.POST["Prescription"],
#                     "consultation_fees":request.POST["Fess"],
#                     "referred_to_doctor":request.POST["referred_to_doctor"],
#                     "referred_by_doctor":request.POST["referred_by_doctor"],
#                     "Followup_DateTime":formatted_datetime,
#                     "appointment_id":request.session['appointment_id'],
#                     "further_assited": 1,
#                     "consultation_datetime":current_epoch_time, 
#                     "consultation_mode": 1,
#                 }
#                 #updateconsult_url="http://localhost:8000/api/update_consultation_details/"
#                 updateconsult_url="http://13.233.211.102/medicalrecord/api/update_consultation_details/"
#                 updateconsult_response=requests.post(updateconsult_url,json=update_consultation)
#                 print(updateconsult_response.text)

#                 all_kco=request.POST['kco']
#                 alladvice=request.POST['advice']
#                 # Splitting the strings by newline characters and removing empty strings
#                 kco_list = [kco.strip() for kco in all_kco.split('\n') if kco.strip()]
#                 advice_list = [advice.strip() for advice in alladvice.split('\n') if advice.strip()]

#                 # Joining the lists into single strings separated by commas
#                 kco_str = ', '.join(kco_list)
#                 advice_str = ', '.join(advice_list)

#                 print(kco_str)
#                 print(advice_str)
#                 update_symptoms= {
#                     "patient_id":patient_id, 
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_status": patient_status,
#                     "findgings_datetime": current_epoch_time, 
#                     "consultation_id":request.session['consultation_id'],
#                     "findings": request.POST["Diagnosis"],
#                     "symtoms": request.POST['complaint_details'],
#                     "kco":kco_str,
#                     "advice":advice_str
#                     }
#                 update_patient_findingsandsymtoms_url = "http://13.233.211.102/medicalrecord/api/update_patient_findings_and_symptoms/"

#                 updatefindingsandsymtoms_response = requests.post(update_patient_findingsandsymtoms_url,json=update_symptoms)
#                 print(updatefindingsandsymtoms_response.text)
#                 # return HttpResponse("done")


               
#                 mode = request.POST.get('Mode')
#                 medicine = request.POST.get('Medicine')
#                 days = request.POST.get('days')
#                 dosage = request.POST.get('dosage')
#                 language = request.POST.get('Language')
#                 instruction = request.POST.get('Instructions')
#                 print(language,instruction,mode,medicine,days,dosage) 
#                 instruction_list= instruction.split(",")
#                 mode_list=mode.split(",")
#                 medicine_list=medicine.split(",")
#                 days_list=days.split(",")
#                 dosage_list=dosage.split(",")
#                 language_list=language.split(",")
#                 print(language_list,instruction_list,mode_list,medicine_list,days_list,dosage_list)
#                 patientmedic_url="http://13.233.211.102/medicalrecord/api/get_patient_medications_byconsultationid/"
#                 api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#                 patientmedic_response=requests.post(patientmedic_url,json=api_para)
#                 patientmedic_data=(patientmedic_response.json().get("message_data"))
#                 medic_list=[]
#                 for i in patientmedic_data:
#                     print(i)
#                     medic_list.append(i)
#                     print("-----------------------")
#                 print(medic_list)
#                 prescription_url="http://13.233.211.102/medicalrecord/api/get_prescription_details/"
#                 api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#                 prescription_response=requests.post(prescription_url,json=api_para)
#                 print(prescription_response.text)
#                 prescription_data=(prescription_response.json().get("message_data"))[0]
#                 print(prescription_data)
#                 # prescription_id=(medic_list[0])['prescription_id']
#                 prescription_id=prescription_data['prescriptions_id']
#                 previous_name={}
#                 for i in medic_list:
#                     previous_name[i['medicine_name']]=i['patient_medication_id']
#                 print(previous_name)
#                 print(medicine_list)
#                 unique_list=[]
#                 u_index=[]
#                 sum=-1
#                 for name in medicine_list:
#                     sum+=1
#                     if(name in previous_name):
#                         continue
#                     else:
#                         u_index.append(sum)
#                         unique_list.append(name)
        
#                 print(unique_list)
#                 print(u_index,'u_index')
#                 print(sum,'sum')

#                 updated_modelist=[ mode_list[i]  for i in u_index]
#                 print("update dmode list",updated_modelist)
#                 updated_dayslist=[ days_list[i]  for i in u_index]
#                 print("update days list",updated_dayslist)
#                 updated_instructionlist=[ instruction_list[i]  for i in u_index]
#                 print("update instruction list",updated_instructionlist)
#                 updated_dosagelist=[ dosage_list[i]  for i in u_index]
#                 print("update dosage list",updated_dosagelist)

#                 # med_id_list=[]
#                 # for name in unique_list:
#                 #     for medicine in all_medicines:
#                 #         if(name==medicine['medicine_name']):
#                 #             med_id_list.append(medicine['doctor_medicine_id'])
#                 if(unique_list and unique_list[0]):
#                     med_id_list=[]
#                     for name in unique_list:
#                       for medicine in all_medicines:
#                           if(name==medicine['medicine_name']):
#                              med_id_list.append(medicine['doctor_medicine_id'])
#                     # medication_url="http://127.0.0.1:8000/api/insert_patient_medications/"
#                     medication_url="http://13.233.211.102/medicalrecord/api/insert_patient_medications/"
#                     for i in range(len(unique_list)):
#                             medication_data={
#                                 "doctor_id": request.session["doctor_id"],
#                                 "patient_id": patient_id,
#                                 "patient_status": patient_status,
#                                 "consultation_id":request.session['consultation_id'],
#                                 "prescription_id":prescription_id,
#                                 "medication_datetime": "2024-02-01 12:30:00",
#                                 "medicine_id": med_id_list[i],
#                                 "medicine_form": updated_modelist[i],
#                                 "medicine_name": unique_list[i],
#                                 "medicine_duration":updated_dayslist[i],
#                                 "medicine_doses": updated_dosagelist[i],
#                                 "medicine_dose_interval": "8 hours",
#                                 "medicine_instruction_id": updated_instructionlist[i],
#                                 "medicine_Category": 7,
#                                 "Medicine_ExtraField1": 8,
#                                 "Medicine_ExtraField2": 9
#                             }
#                             response=requests.post(medication_url,json=medication_data)
#                             print(response.text)

#                 common_name=[]
#                 for i in medicine_list:
#                     if(i in unique_list):
#                         continue
#                     else:
#                         common_name.append(i)
#                 print(common_name,"common Name")

#                 delete_medic=[]
#                 for key, value in previous_name.items():
#                     if key not in common_name:
#                         delete_medic.append(key)
#                         deletemedic_url=" http://13.233.211.102/medicalrecord/api/delete_patient_medications/"
#                         deletemedic_response=requests.post(deletemedic_url,json={"Patient_Medication_Id":value})
#                         print(deletemedic_response.text)
                         
#                 print(delete_medic)

#                 labs=request.POST['lab_tests']
#                 labsdata_list = [labs.strip() for labs in labs.split('\n') if labs.strip()]
#                 print('from screen',labsdata_list)
#                 patientlab_url="http://13.233.211.102/medicalrecord/api/get_patient_labinvestigations_by_consultation_id/"
#                 api_para={"consultation_id":get_patient_by_appointment_id.get('consultation_id')}
#                 patientlab_response=requests.post(patientlab_url,json=api_para)
#                 patientlab_data=(patientlab_response.json().get("message_data"))
#                 lab_list={}
#                 for i in patientlab_data:
#                     print(i)
#                     lab_list[i['labinvestigation_category']]=i['patient_labinvestigation_id']
#                     print("-----------------------")
#                 print('get data',lab_list)
#                 unique_lablist=[]
#                 for i in labsdata_list:
#                     if(i in lab_list):
#                         continue
#                     else:
#                         unique_lablist.append(i)
#                 print(unique_lablist)
#                 if(unique_lablist):
#                     # lab_url="http://localhost:8000/api/insert_patient_labinvestigations/"
#                     lab_url="http://13.233.211.102/medicalrecord/api/insert_patient_labinvestigations/"
#                     labs_data={
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_id": patient_id,
#                     "patient_status": patient_status,
#                     "consultation_id": request.session['consultation_id'],
#                     "prescription_id": prescription_id,
#                     "labinvestigation_datetime": "2022-02-11 14:30:00",
#                     # "labinvestigation_category": 2,
#                     "patient_labtestid": 1,#investigation_id
#                     "patient_labtestreport": "Sample Report",
#                     "patient_labtestsample": 3,
#                     "patient_labtestreport_check": 1,
#                     "lattest_extrafield1": 42,
#                     "isdeleted":0
#                     }
#                     for category in unique_lablist:
#                         labs_data['labinvestigation_category']=category
#                         lab_response=requests.post(lab_url,json=labs_data)
#                     print(lab_response.text)
                
#                 common_labname=[]
#                 for i in labsdata_list:
#                     if(i in unique_lablist):
#                         continue
#                     else:
#                         common_labname.append(i)
#                 print(common_labname,"common lab Name")
#                 delete_lab=[]
#                 for key, value in lab_list.items():
#                     if key not in common_labname:
#                         delete_lab.append(key)
#                         deletelab_url=" http://13.233.211.102/medicalrecord/api/delete_patient_labinvestigations/"
#                         deletelab_response=requests.post(deletelab_url,json={"Patient_LabInvestigation_Id":value})
#                         print(deletelab_response.text)
                         
#                 print(delete_lab)
            
# #####################Update prescription details######################
#                 prescritption=request.POST['Prescription']
#                 print(prescritption)
#                 # updateprescription_url="http://localhost:8000/api/update_prescription_details/"
#                 updateprescription_url="http://13.233.211.102/medicalrecord/api/update_prescription_details/"
#                 prescription_data={
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_id": patient_id,
#                     "patient_status": patient_status,
#                     "consultation_id":request.session['consultation_id'],
#                     "prescription_datetime": current_epoch_time,
#                     "prescription_details": prescritption
#                 }
#                 updateprescritption_response=requests.post(updateprescription_url,json=prescription_data)
#                 print(updateprescritption_response.text)

#                 api_data = {
#                     "Doctor_Id":request.session["doctor_id"],
#                     "Patient_Id":patient_id,
#                     "Patient_Status":patient_status,
#                     "Consultation_DateTime":request.POST["Consultation_DateTime"],
#                     "patient_heartratepluse":request.POST["Patient_HeartRatePluse"],
#                     "patient_bpsystolic":request.POST["Patient_BPSystolic"],
#                     "patient_bpsystolic":request.POST["Patient_BPDistolic"],
#                     "patient_painscale":request.POST["Patient_PainScale"],
#                     "patient_respiratoryrate":request.POST["Patient_RespiratoryRate"],
#                     "patient_temparature":request.POST["Patient_Temparature"],
#                     "patient_chest":request.POST["Patient_Chest"],
#                     "patient_ecg":request.POST["Patient_ECG"],
#                     "weight":request.POST['weight'],
#                     "further_assited":"0",
#                     'appointment_id':request.session['appointment_id'],
#                     "consultation_id":request.session['consultation_id']  
#                 }
#                 # url="http://localhost:8000/api/update_patientvitals_by_appointment_id/"
#                 url="http://13.233.211.102/medicalrecord/api/update_patientvitals_by_appointment_id/"
#                 response=requests.post(url,json=api_data)
#                 print(response.text)


#                 #return HttpResponse("done")
#                 return redirect(Consultation)
            
#             else:

#                 insert_consultation = {
#                     "Patient_Id": patient_id,
#                     "Doctor_Id":request.session["doctor_id"] ,
#                     "Patient_Status":patient_status,
#                     "Consultation_DateTime":consultation_datetime,#appointment_datetime
#                     "instructions":request.POST["Prescription"],
#                     "consultation_fees":request.POST["Fess"],
#                     "referred_to_doctor":request.POST["referred_to_doctor"],
#                     "referred_by_doctor":request.POST["referred_by_doctor"],
#                     "Followup_DateTime":formatted_datetime,
#                     "appointment_id":request.session['appointment_id'],
#                     'consultation_status':1
#                 }
#                 consultation_api_url = 'http://13.233.211.102/medicalrecord/api/insert_consultation'

#                 consultation_response = requests.post(consultation_api_url, json=insert_consultation)
#                 print("consultation_response : ", consultation_response.text)
#                 consultation = consultation_response.json().get('message_data', {})
#                 consultation_id=consultation['consultation_id']
#                 print("consultation_ID : ", consultation)
#                 #update appointment status to 3 means completed.
#                 # update_status_url="http://13.233.211.102/appointment/api/update_appointment_status"
#                 # status_response=requests.post(update_status_url,json={"appointment_id":request.session['appointment_id'],"appointment_status":3})
#                 # print(status_response.text)
#                 consultation_id = consultation['consultation_id']
#                 print(consultation_id )
#                 request.session[ 'consultation_id' ] = consultation_id   # Create Session for Consulation ID


#     # ################################ insert_patient__vitals ###############################################

#                 api_data = {
#                     "Doctor_Id":request.session["doctor_id"],
#                     "Patient_Id":patient_id,
#                     "Patient_Status":patient_status,
#                     "Consultation_DateTime":request.POST["Consultation_DateTime"],
#                     "patient_heartratepluse":request.POST["Patient_HeartRatePluse"],
#                     "patient_bpsystolic":request.POST["Patient_BPSystolic"],
#                     "patient_bpsystolic":request.POST["Patient_BPDistolic"],
#                     "patient_painscale":request.POST["Patient_PainScale"],
#                     "patient_respiratoryrate":request.POST["Patient_RespiratoryRate"],
#                     "patient_temparature":request.POST["Patient_Temparature"],
#                     "patient_chest":request.POST["Patient_Chest"],
#                     "patient_ecg":request.POST["Patient_ECG"],
#                     "weight":request.POST['weight'],
#                     "further_assited":"0",
#                     'appointment_id':request.session['appointment_id'],
#                     "consultation_id":consultation_id   
#             }
#                 # url="http://localhost:8000/api/update_patientvitals_by_appointment_id/"
#                 url="http://13.233.211.102/medicalrecord/api/update_patientvitals_by_appointment_id/"
#                 response=requests.post(url,json=api_data)
#                 print(response.text)
                
#     ###############################  insert finding symptoms(complaints & Diagnosis) ########################################
#                 all_kco=request.POST['kco']
#                 alladvice=request.POST['advice']
#                 # Splitting the strings by newline characters and removing empty strings
#                 kco_list = [kco.strip() for kco in all_kco.split('\n') if kco.strip()]
#                 advice_list = [advice.strip() for advice in alladvice.split('\n') if advice.strip()]

#                 # Joining the lists into single strings separated by commas
#                 kco_str = ', '.join(kco_list)
#                 advice_str = ', '.join(advice_list)

#                 print(kco_str)
#                 print(advice_str)
#                 finding_symptoms= {
#                     "patient_id":patient_id, 
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_status": patient_status,
#                     "findgings_datetime": "2023-12-15 15:10:28", 
#                     "consultation_id":consultation_id,
#                     "findings": request.POST["Diagnosis"],
#                     "symtoms": request.POST['complaint_details'],
#                     "kco":kco_str,
#                     "advice":advice_str

#                     }
#                 insert_patient_findingsandsymtoms_url = "http://13.233.211.102/medicalrecord/api/insert_patient_findingsandsymtoms/"

#                 findingsandsymtoms_response = requests.post(insert_patient_findingsandsymtoms_url,json=finding_symptoms)
#                 print(findingsandsymtoms_response.text)

#     #################################Prescription###############################
#                 prescritption=request.POST['Prescription']
#                 print(prescritption)
#                 prescription_url="http://13.233.211.102/medicalrecord/api/insert_prescriptions/"
#                 prescription_data={
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_id": patient_id,
#                     "patient_status": patient_status,
#                     "consultation_id":consultation_id,
#                     "prescription_datetime": "2024-02-01 12:30:00",
#                     "prescription_details": prescritption
#                 }
#                 prescritption_response=requests.post(prescription_url,json=prescription_data)
#                 print(prescritption_response.text)
#                 prescription_id=(prescritption_response.json().get("message_data"))[0]['Prescriptions_Id']
#                 print("prescroption id:",prescription_id)
                
#     #############################Patient Medications##############################
#                 mode = request.POST.get('Mode')
#                 medicine = request.POST.get('Medicine')
#                 days = request.POST.get('days')
#                 dosage = request.POST.get('dosage')
#                 language = request.POST.get('Language')
#                 instruction = request.POST.get('Instructions')
#                 print('language',language,'instruction',instruction,'mode',mode,'medicine',medicine,'days',days,'dosage',dosage) 
#                 instruction_list= instruction.split(",")
#                 mode_list=mode.split(",")
#                 medicine_list=medicine.split(",")
#                 days_list=days.split(",")
#                 dosage_list=dosage.split(",")
#                 language_list=language.split(",")
#                 med_id_list=[]
#                 for name in medicine_list:
#                     print("name",name)
#                     for medicine in all_medicines:
#                         if(name==medicine['medicine_name']):
#                             med_id_list.append(medicine['doctor_medicine_id'])
            
                
#                 if medicine_list[0]:
#                     # medication_url="http://127.0.0.1:8000/api/insert_patient_medications/"
#                     medication_url="http://13.233.211.102/medicalrecord/api/insert_patient_medications/"
#                     for i in range(len(medicine_list)):
#                             medication_data={
#                                 "doctor_id": request.session["doctor_id"],
#                                 "patient_id": patient_id,
#                                 "patient_status": patient_status,
#                                 "consultation_id":consultation_id,
#                                 "prescription_id":prescription_id,
#                                 "medication_datetime": "2024-02-01 12:30:00",
#                                 "medicine_id": med_id_list[i],
#                                 "medicine_form": mode_list[i],
#                                 "medicine_name": medicine_list[i],
#                                 "medicine_duration":days_list[i],
#                                 "medicine_doses": dosage_list[i],
#                                 "medicine_dose_interval": "8 hours",
#                                 "medicine_instruction_id": instruction_list[i],
#                                 "medicine_Category": 7,
#                                 "Medicine_ExtraField1": 8,
#                                 "Medicine_ExtraField2": 9
#                             }
#                             response=requests.post(medication_url,json=medication_data)
#                             print(response.text)
#                 # print(language_list,instruction_list,mode_list,medicine_list,days_list,dosage_list,med_id_list)
#                 # print(all_medicines)
#                 # print(med_id_list)
#                 # return HttpResponse("ok")

#                 else:
#                     print("no data")
                
#     ##############################Patient Lab Investigations###########################
#                 labs=request.POST['lab_tests']
#                 labs_list = [labs.strip() for labs in labs.split('\n') if labs.strip()]
#                 labinvest_id=[]
#                 print(labs_list)
#                 if(labs_list):
#                     # lab_url="http://localhost:8000/api/insert_patient_labinvestigations/"
#                     lab_url="http://13.233.211.102/medicalrecord/api/insert_patient_labinvestigations/"
#                     labs_data={
#                     "doctor_id": request.session["doctor_id"],
#                     "patient_id": patient_id,
#                     "patient_status": patient_status,
#                     "consultation_id": consultation_id,
#                     "prescription_id": prescription_id,
#                     "labinvestigation_datetime": "2022-02-11 14:30:00",
#                     # "labinvestigation_category": 2,
#                     "patient_labtestid": 1,#investigation_id
#                     "patient_labtestreport": "Sample Report",
#                     "patient_labtestsample": 3,
#                     "patient_labtestreport_check": 1,
#                     "lattest_extrafield1": 42,
#                     "isdeleted":0
#                 }
#                     for category in labs_list:
#                         labs_data['labinvestigation_category']=category
#                         lab_response=requests.post(lab_url,json=labs_data)
#                     print(lab_response.text)
#                 else:
#                     print("no labs found")
                
#                 # return redirect(get_all_doctor_appointments)
#                 return redirect(Consultation)