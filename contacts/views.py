from django.contrib.messages.api import error
from contacts.models import Contact, ContactModel
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.

def inquiry(request):

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        car_id  = request.POST["car_id"]
        customer_need = request.POST["customer_need"]
        car_title = request.POST["car_title"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]

        form = Contact(first_name = first_name, last_name = last_name, car_title = car_title, 
        car_id = car_id, customer_need = customer_need, city = city, state = state, email = email,
        phone = phone, message = message,user_id = user_id)

        form.save()
        send_mail(

            'Başlıq',
            'Bura mesaj yeridi.',
            'xelilovmiz@gmail.com',
            [email],
            fail_silently=False,
            )

        if request.user.is_authenticated:

            user_id= request.POST["user_id"]
            car_id = request.POST["car_id"]

            data = Contact.objects.filter(user_id = user_id, car_id =car_id)

            if data:

                messages.info(request,"Siz artıq bu maşın haqqında göndərmə etmisiniz.")
                return redirect("/cars/car_detail/"+car_id)


    return redirect("/cars/car_detail/"+car_id)


def contactme(request):

    if request.method == "POST":
        name = request.POST["name"]
        email =request.POST["email"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        message= request.POST["message"]

        contact = ContactModel(name = name, email = email, 
        subject = subject, 
        phone = phone, message = message)

        contact.save()
        send_mail(

            "Carzone",
            'Hörmətli ' + name + " Sizin mesajınız şirkətimizə çatmışdır. Mesajınıza baxıldıqdan sonra sizinlə əlaqə saxlanılacaq",
            'xelilovmiz@gmail.com',
            [email],
            fail_silently=False,
            )        
        messages.success(request,"Mesajınız uğurla göndərildi.")
        return redirect("pages:contact")

    return render(request,"pages/contact.html")