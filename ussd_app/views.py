from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import datetime 
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

           
class USSDEventView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        resp =request.data
        d_status = resp['status']
        date =resp['date']
        input = resp['input']
        networkcode = resp['networkCode']
        session_id = resp['sessionId']
        hops_count = resp['hopsCount']
        service_code = resp['serviceCode']
        error_message = resp['errorMessage']
        last_app_resp = resp['lastAppResponse']
        duration_in_millis = resp['durationInMillis']
        phone_number = resp['phoneNumber']
        
        data = { }
        data['status'] = d_status
        data['date'] = date
        data['input'] = input
        data['networkcode'] = networkcode
        data['session_id'] = session_id
        data['phone_number'] = phone_number
        data['duration'] = duration_in_millis
        data['error_message'] = error_message
        data['service_code'] = service_code
        
        print ('The event resp: ', data)
        print (resp)
        
        
        return Response ('Done',status=status.HTTP_200_OK)  
    
def quick_saver(text):  
    if text == '1*1':
        response = 'CON What is your Firstname ?'
    
    elif text.count('*') == 2 and text.split('*')[:2]== ['1', '1'] :
        firstname= text.split('*')[2]
        print ('firstname:',firstname)

        response = 'CON What is your Lastname ?'
    
    elif text.count('*') == 3 and text.split('*')[:2]== ['1', '1'] :
        lastname= text.split('*')[3]
        print ('lastname:',lastname)
        response = 'CON What is your Sex( M or F) ?' 
        
    elif text.count('*') == 4 and text.split('*')[:2]== ['1', '1'] :
        sex= text.split('*')[4]
        lname = text.split('*')[3]
        fname = text.split('*')[2]
        response = 'END Quick Saver account created successfully.\nBelow are filled data: \n'
        response += f'Firstname: {fname} \n'
        response += f'Lastname: {lname} \n'
        response += f'Sex: {sex}'
        
        data = { }  
        data['Firstname'] = fname
        data['lastname'] = lname
        data['Sex'] = sex
        print ('data:',data)
    return response
    
    
def premium_saver(text):  
    if text == '1*2':
        response = 'CON What is your Company Name ?'
    
    elif text.count('*') == 2 and text.split('*')[:2]== ['1', '2'] :
        company= text.split('*')[2]
        print ('firstname:',company)

        response = 'CON What is your Lastname ?'
    
    elif text.count('*') == 3 and text.split('*')[:2]== ['1', '2'] :
        lastname= text.split('*')[3]
        print ('lastname:',lastname)
        response = 'CON What is your Firstname ?' 

    elif text.count('*') == 4 and text.split('*')[:2]== ['1', '2'] :
        firstname= text.split('*')[4]
        print ('lastname:',firstname)
        response = 'CON What is your Sex (M or F) ?' 
        
    elif text.count('*') == 5 and text.split('*')[:2]== ['1', '2'] :
        sex= text.split('*')[5]
        lname = text.split('*')[3]
        fname = text.split('*')[4]
        comp = text.split('*')[2]
        response = 'END Medium Saver account created successfully.\nBelow are filled data: \n'
        response += f'Registered Company: {comp} \n'
        response += f'Firstname: {fname} \n'
        response += f'Lastname: {lname} \n'
        response += f'Sex: {sex}'
        
        data = { }  
        data['Firstname'] = fname
        data['lastname'] = lname
        data['Company'] = comp
        data['Sex'] = sex
        print ('data:',data)
    else:
        response = "END  Invalid Input"
        
    return response


def main_activity(text,phone_number):
    if text =='' or text.split('*')[-1]== '0':
        response = 'CON Welcome to Sunnex Service \n'
        response += 'Our Services are: \n '
        response += '1. Create Account \n'
        response += '2. Check Balance \n'
        response += '3. Show Number \n'
        response += '0. Back to the menu '

        
    elif text == '1':
        response = 'CON What type of Account do you want to create ? \n'
        response += '1. Quick Savers \n'
        response += '2. Premium Savers \n'
        response += '0. Back to the menu '
    
    
    elif text[:3]== '1*1':
        response = quick_saver(text)
    
    elif text[:3]== '1*2':
        response = premium_saver(text)
    
    elif text == '2':
        response = "END  Your account balance is $1,020,500"

    elif text == '3':
        response = f"END  Your number is {phone_number}"  
        
    else:
        response = "END  Invalid Input"
     
    return response



@csrf_exempt
def ussd_view(request):
    resp =request.POST
    print (resp)
    phone_number = resp['phoneNumber'] if resp['phoneNumber'] else None
    service_code = resp['serviceCode']  if resp['serviceCode'] else None
    network_code = resp['networkCode']  if resp['networkCode'] else None
    session_id = resp['sessionId']
    text = resp['text']
    print ('text:',text)
    if '0' in text :
        new_text = text[text.index('0')+2:]
        print(new_text)
        response=main_activity(new_text,phone_number)
    else:
        response=main_activity(text,phone_number)
    
    
    return HttpResponse(response) 
    
    
