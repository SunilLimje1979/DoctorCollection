from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',doctorReg),
    path('addclinic/',addClinic),
    path('addslot/',addSlot),
    path('consultfee/',consultaion_fee),
    path("pdf_view/",pdf_view),
    path("dashboard/",dashboard),
    path("no_service/",no_service),
    path("settingdashboard/",settingdashboard),
    path('fetch-timings/', fetch_timings, name='fetch_timings'),
    path("leavesystem/",leavesystem),
    path("leaves/",leaves),
    path("updateleave/<leave_date>/",updateleave),
    path("opdlogin/",opdlogin1),
    path("opdlogin/<token>/",opdlogin),
    ############################New merged####################################
    path("insert_medicine/",insert_medicine ,name="insert_medicine"),
    path("get_all_medicines/",get_all_medicines,name='get_all_medicines'),
    path('update_medicine/<int:doctor_medicine_id>/',update_medicine,name='update_medicine'),
    path("delete_medicine/<int:doctor_medicine_id>/",delete_medicine,name='delete_medicine'),
    path("add_lab_report/",add_lab_report,name='add_lab_report'),
    path("get_all_lab_report/",get_all_lab_report,name='get_all_lab_report'),
    path("update_lab_report/<int:investigation_id>/",update_lab_report,name='update_lab_report'),
    path("delete_lab_report/<int:investigation_id>/",delete_lab_report,name='delete_lab_report'),
    path('get_all_doctor_appointments/',get_all_doctor_appointments,name='get_all_doctor_appointments'),
    path("fetch_data/",fetch_data,name='fetch_data'),
    path('initial_assesment/<int:appointment_id>',initial_assesment,name='initial_assesment'),
    path('update_initial_assesment/',update_initial_assesment,name='update_initial_assesment'),
    path('consultation/',consultation,name='consultation'),
    # path("consultpdf/",showpdf,name='consultpdf'),
    # path('consultation/',consultation,name='consultation'),
     
]