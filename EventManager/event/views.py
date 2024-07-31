from django.conf import settings
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from event.models import Team, Client, Work, Rate, BookEvent


# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'home.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')
    return render(request, 'signin.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if not username or not password:
            messages.error(request, 'fields are empty')
            return render(request, 'signup.html')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username taken")
                return render(request, "signup.html")
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('/signin')
        else:
            messages.error(request, "password does not match")
            return render(request, 'signup.html')

    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def viewteam(request):
    team=Team.objects.all()
    return render(request,'team.html',{'team':team})


def profile(request):
    if request.method == 'POST':
        # Retrieve the username from the POST request
        username_str = request.POST.get('username')

        try:
            # Retrieve the User instance
            username = User.objects.get(username=username_str)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'profile.html')

        name = request.POST.get('name')
        phno = request.POST.get('phone')
        email = request.POST.get('email')

        # Create and save the Client instance
        details = Client(
            username=username,  # Assigning User instance
            Name=name,
            Phno=phno,
            Email=email
        )
        details.save()
        messages.success(request, 'Added successfully')

    return render(request, 'profile.html')

def bookevent(request):
        event_types=Work.objects.all()

        prices = Rate.objects.all()


        if request.method == 'POST':
            event_type_id = request.POST.get('event_type')
            booking_date = request.POST.get('booking_date')
            price_type_id = request.POST.get('price_type')  # Get the price from the form

            event_type = get_object_or_404(Work, id=event_type_id)
            price_type=get_object_or_404(Rate,id=price_type_id)

            if not booking_date:
                messages.error(request, 'Booking date is required.')
                return render(request, 'booking.html', {'event_types': event_types,'prices':prices})

            # Check if the booking date is in the past
            if booking_date < str(timezone.now().date()):
                messages.error(request, "You can't book on that date")
                return render(request, 'booking.html', {'event_types': event_types,'prices':prices})

            # Check if the date is already booked
            if BookEvent.objects.filter(event_type=event_type, booking_date=booking_date).exists():
                messages.error(request, 'This date is already booked.')
                return render(request, 'booking.html', {'event_types': event_types,'prices':prices})

            BookEvent.objects.create(
                user=request.user,
                event_type=event_type,
                price=price_type,  # Save the price in the BookEvent model
                booking_date=booking_date,
            )
            messages.success(request, 'Booking successful')
            return redirect('book')

        return render(request, 'booking.html', {'event_types': event_types,'prices':prices})

