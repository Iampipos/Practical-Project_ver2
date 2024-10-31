from django.shortcuts import render
from dotenv import load_dotenv
import os
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import UserProfile, TourType
from django.contrib import messages

load_dotenv()
API_KEY = os.getenv('API_KEY')



# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def traveldetail(request,place_id):
    print (place_id)
    url = f'https://tatapi.tourismthailand.org/tatapi/v5/attraction/{place_id}'  # เปลี่ยน 'endpoint' ให้เป็น endpoint ที่คุณต้องการเรียกใช้
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'Accept-Language':'th'
    }
    params = {
      "place_id":place_id# เพิ่มพารามิเตอร์ที่ API ต้องการ เช่น 'category': 'temples' เป็นต้น
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
    # print(data)
    return render(request, 'traveldetail.html',data)



def get_tourist_data(request):
    url = 'https://tatapi.tourismthailand.org/tatapi/v5/places/search?keyword=ภูเขา'  # เปลี่ยน 'endpoint' ให้เป็น endpoint ที่คุณต้องการเรียกใช้
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'Accept-Language':'th'
    }
    params = {
      "keyword":"ภูเขา" # เพิ่มพารามิเตอร์ที่ API ต้องการ เช่น 'category': 'temples' เป็นต้น
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)

def get_transport_data(request):
    url = "https://datagov.mot.go.th/api/3/action/datastore_search?resource_id=7adf3707-942d-49bc-a8d3-fa9f595f394c"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # ตรวจสอบว่าการดึงข้อมูลสำเร็จ
        data = response.json()  # แปลงข้อมูลเป็น JSON
        return JsonResponse(data, safe=False)
    except requests.exceptions.RequestException as e:
        # จัดการกรณีที่เกิดข้อผิดพลาดในการดึงข้อมูล
        return JsonResponse({'error': str(e)}, status=500)
    

def register(request):
    if request.method == 'POST':
        # รับข้อมูลจากฟอร์ม
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gender']
        age_group = request.POST['age_group']
        favorite_types_ids = request.POST.getlist('favorite_types')  # รับค่าประเภทการท่องเที่ยวที่เลือกเป็น list

        # สร้างโปรไฟล์ผู้ใช้ใหม่และบันทึกข้อมูล
        user_profile = UserProfile.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            age_group=age_group
        )
        user_profile.favorite_types.set(favorite_types_ids)  # ตั้งค่าประเภทการท่องเที่ยวที่ชื่นชอบ
        user_profile.save()

        messages.success(request, 'ลงทะเบียนสำเร็จ')
        return redirect('home')

    # ดึงประเภทการท่องเที่ยวทั้งหมดเพื่อใช้ในฟอร์ม
    tour_types = TourType.objects.all()
    return render(request, 'register.html', {'tour_types': tour_types})

def get_detail_data(request):
    url = 'https://tatapi.tourismthailand.org/tatapi/v5/attraction/P03019076'  # เปลี่ยน 'endpoint' ให้เป็น endpoint ที่คุณต้องการเรียกใช้
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'Accept-Language':'th'
    }
    params = {
      "place_id":"P03019076" # เพิ่มพารามิเตอร์ที่ API ต้องการ เช่น 'category': 'temples' เป็นต้น
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)
