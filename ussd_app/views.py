from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import datetime 
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.

           
class USSDView(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        resp =request.data
        print (resp)
        phone_number = resp['phoneNumber'] if resp['phoneNumber'] else None
        service_code = resp['serviceCode']  if resp['serviceCode'] else None
        network_code = resp['networkCode']  if resp['networkCode'] else None
        session_id = resp['sessionId']
        text = resp['text']
        print ('text:',text)
        
        if text == ' ':
            response = 'CON Welcome to Sunnex Service'
            response += 'Our Services are: \n '
            response += '1. Create Account \n'
            response += '2. Check Balacne \n'
            response += '3. Show Number'
            
        elif text == '1':
            print ('here')
            response = "END Account Created Successfully"
            
        elif text == '2':
            response = "END  Your account balance is $1,020,500"

        elif text == '3':
            response = "END  Your number is 08067715394"  
            response.headers['Content-Type'] = "text/plain"          
            
        else:
            response = "END  Invalid Input"
            
            
        return Response (response)   
    

data = { }  

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
        response += '4. Premium Savers '
        
    elif text == '1*1':
        response = 'CON What is your Firstname?'
    
    elif text.count('*') == 2 and text.split('*')[:2]== ['1', '1'] :
        firstname= text.split('*')[2]
        data['firstname'] = firstname
        print ('firstname:',firstname)

        response = 'CON What is your Lastname '
    
    elif text.count('*') == 3 and text.split('*')[:2]== ['1', '1'] :
        lastname= text.split('*')[3]
        print ('lastname:',lastname)
        data['lastname'] = lastname
        response = 'CON What is your Sex' 
        
    elif text.count('*') == 4 and text.split('*')[:2]== ['1', '1'] :
        sex= text.split('*')[4]
        lname = text.split('*')[3]
        fname = text.split('*')[2]
        response = 'END Your Registration was successful. Below are filled data \n'
        response += f'Firstname: {fname} \n'
        response += f'Lastname: {lname} \n'
        response += f'Sex: {sex}'

        print ('data:',data)
    
    elif text.split('*')[-1]== '0' :
        sex= text.split('*')[4]
        data['sex'] =sex
        response = 'END Your Registration was successful'
        print ('data:',data)
    
        

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
        response=d_text(text)
    else:
        response=d_text(text)
    
    
    return HttpResponse(response) 
    
    
