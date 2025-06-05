from django.shortcuts import render, redirect
from contacts.models import Contact
from django.contrib import messages

def contact(request):
	
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        realtor_email = request.POST["realtor_email"]
        user_id = request.POST["user_id"]
        if request.user.is_authenticated:
            print("request user id", request.user.id)
            print("user_id", user_id)
            # has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=request.user.id)
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You has already inquired this listing")
                return redirect('listings:listing', listing_id=listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name,
                          email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        #return redirect("accounts:dashboard") #redirect to app accounts function dashboard
        return redirect('listings:listing', listing_id=listing_id)

def delete_contact(request,contact_id):
	return redirect("accounts:dashboard")