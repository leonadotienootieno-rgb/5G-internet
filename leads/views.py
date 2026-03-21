from django.shortcuts import render, redirect
from .forms import LeadForm
from django.core.mail import send_mail

def landing(request):

    step = 1
    estate = ''
    apartment = ''

    if request.method == "POST":

        # STEP 1: Availability check
        if 'check_availability' in request.POST:
            estate = request.POST.get('estate')
            apartment = request.POST.get('apartment')

            request.session['estate'] = estate
            request.session['apartment'] = apartment

            step = 2

        # STEP 2: Submit lead
        elif 'submit_lead' in request.POST:
            form = LeadForm(request.POST)

            if form.is_valid():
                lead = form.save(commit=False)

                # attach session data
                lead.estate = request.session.get('estate')
                lead.apartment = request.session.get('apartment')

                lead.save()

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

    return render(request, 'landing.html', {
        'step': step,
        'form': LeadForm(),
        'estate': estate,
        'apartment': apartment
    })


def thankyou(request):
    return render(request, 'thankyou.html')