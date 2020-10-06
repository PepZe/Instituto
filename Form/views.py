from django.shortcuts import render
from .models import Register
from datetime import datetime
from .Business import send_email, qr_code_generator
import os


current_path = os.path.abspath(os.getcwd())
from_email = ""
password = ""


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        church = request.POST['church']
        phone = request.POST['phone']
        date = request.POST['date']

        arrayDate = date.split('-')
        year = int(arrayDate[0])
        month = int(arrayDate[1])
        day = int(arrayDate[2])

        model = Register(name=name, email=email, church=church,
                         date=datetime(year, month, day), phone=phone)

        file_name = "convite.png"
        qr_code = qr_code_generator.qr_code()
        qr_code.create('{0}; {1}; {2}; {3}; {4}; {5}'.format(
            name, email, church, model.date, phone, model.check_in), file_name)

                
        gmail = send_email.Email(from_email, password)
        gmail.send_email(email, "Instituto", "Vai ser legal",
                         '{0}\{1}'.format(current_path, file_name))
        
        os.remove(file_name)

    return render(request, 'index.html')
