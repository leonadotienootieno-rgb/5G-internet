from django.shortcuts import render, redirect
from .forms import LeadForm
from django.core.mail import send_mail

def landing(request):

    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save()

            send_mail(
                'New 5G Installation Lead',
                f"""
New lead received

Name: {lead.name}
Phone: {lead.phone}
Estate: {lead.estate}
Apartment: {lead.apartment}
Message: {lead.message}
                """,
                'leonadotienootieno@gmail.com',
                ['leonadotienootieno@gmail.com'],
            )

            return redirect('thankyou')

    else:
        form = LeadForm()

    return render(request,'landing.html',{'form':form})


def thankyou(request):
    return render(request,'thankyou.html')
