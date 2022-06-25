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
        print (resp)
        
        return Response ('Done',status=status.HTTP_200_OK)  
    
def quick_saver (text):  
    if text == '1*1':
        response = 'CON What is your Firstname?'
    
    elif text.count('*') == 2 and text.split('*')[:2]== ['1', '1'] :
        firstname= text.split('*')[2]
        print ('firstname:',firstname)

        response = 'CON What is your Lastname '
    
    elif text.count('*') == 3 and text.split('*')[:2]== ['1', '1'] :
        lastname= text.split('*')[3]
        print ('lastname:',lastname)
        response = 'CON What is your Sex' 
        
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
    
    
def medium_saver (text):  
    if text == '2*1':
        response = 'CON What is your Company Name?'
    
    elif text.count('*') == 2 and text.split('*')[:2]== ['2', '1'] :
        company= text.split('*')[2]
        print ('firstname:',company)

        response = 'CON What is your Lastname '
    
    elif text.count('*') == 3 and text.split('*')[:2]== ['1', '1'] :
        lastname= text.split('*')[3]
        print ('lastname:',lastname)
        response = 'CON What is your Sex' 

    elif text.count('*') == 4 and text.split('*')[:2]== ['1', '1'] :
        firstname= text.split('*')[4]
        print ('lastname:',firstname)
        response = 'CON What is your Sex' 
        
    elif text.count('*') == 5 and text.split('*')[:2]== ['1', '1'] :
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
    return response


def d_text(text):
    if text =='' or text.split('*')[-1]== '0':
        response = 'CON Welcome to Sunnex Service'
        response += 'Our Services are: \n '
        response += '1. Create Account \n'
        response += '2. Check Balacne \n'
        response += '3. Show Number'
        
    elif text == '1':
        response = 'CON What type of Account do you want to create ? \n'
        response += '1. Quick Savers \n'
        response += '2. Medium Savers \n'
        response += '3. Gold Savers \n'
        response += '4. Premium Savers  \n'
        response += '0. Back to the menu '
    
    elif text[:2]== '1*':
        response = quick_saver(text)
    
    elif text == '2':
        response = "END  Your account balance is $1,020,500"

    elif text == '3':
        response = "END  Your number is 08067715394"  
        
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
        response=d_text(new_text)
    else:
        response=d_text(text)
    
    
    return HttpResponse(response) 
    
    
