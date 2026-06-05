from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
 
from .forms import ContactForm
 
from .forms import (
    ITRRequestForm,
    GSTRequestForm,
    TDSRequestForm,
    BookkeepingRequestForm
)
 
from .models import (
    ITRAdditionalDocument,
    GSTAdditionalDocument,
    TDSAdditionalDocument,
    BookkeepingAdditionalDocument
)
 
 
# =========================
# HOME PAGE
# =========================
 
def home(request):
 
    return render(request, 'home.html')
 
 
# =========================
# ABOUT PAGE
# =========================
 
def about(request):
 
    return render(request, 'about.html')
 
 
# =========================
# SERVICES PAGE
# =========================
 
def services(request):
 
    return render(request, 'services.html')
 
 
# =========================
# CONTACT PAGE
# =========================
 
def contact(request):
 
    form = ContactForm()
 
    if request.method == 'POST':
 
        form = ContactForm(request.POST)
 
        if form.is_valid():
 
            full_name = form.cleaned_data['full_name']
 
            email = form.cleaned_data['email']
 
            message = form.cleaned_data['message']
 
            # EMAIL TO ADMIN
 
            send_mail(
 
                subject='New Contact Message',
 
                message=f'''
Name: {full_name}
 
Email: {email}
 
Message: {message}
''',
 
                from_email=settings.EMAIL_HOST_USER,
 
                recipient_list=[
                    settings.EMAIL_HOST_USER
                ],
 
                fail_silently=False,
            )
 
            # EMAIL TO USER
 
            send_mail(
 
                subject='Message Received',
 
                message=f'''
Hello {full_name},
 
We have received your message.
 
Our team will contact you soon.
 
Thank you.
''',
 
                from_email=settings.EMAIL_HOST_USER,
 
                recipient_list=[email],
 
                fail_silently=False,
            )
 
            return redirect('success')
 
    return render(
        request,
        'contact.html',
        {'form': form}
    )
 
 
# =========================
# SUCCESS PAGE
# =========================
 
def success(request):
 
    return render(request, 'success.html')
 
 
# =========================
# COMMON FORM HANDLER
# =========================
 
def handle_form(request, form_class, template_name):
 
    if request.method == 'POST':
 
        form = form_class(
            request.POST,
            request.FILES
        )
 
        if form.is_valid():
 
            # SAVE MAIN REQUEST
 
            saved_request = form.save()
 
            # GET ADDITIONAL FILES
 
            other_files = request.FILES.getlist(
                'other_documents'
            )
 
            # SAVE ADDITIONAL FILES
 
            for file in other_files:
 
                if form_class == ITRRequestForm:
 
                    ITRAdditionalDocument.objects.create(
                        itr_request=saved_request,
                        document=file
                    )
 
                elif form_class == GSTRequestForm:
 
                    GSTAdditionalDocument.objects.create(
                        gst_request=saved_request,
                        document=file
                    )
 
                elif form_class == TDSRequestForm:
 
                    TDSAdditionalDocument.objects.create(
                        tds_request=saved_request,
                        document=file
                    )
 
                elif form_class == BookkeepingRequestForm:
 
                    BookkeepingAdditionalDocument.objects.create(
                        bookkeeping_request=saved_request,
                        document=file
                    )
 
            # EMAIL TO ADMIN
 
            send_mail(
 
                subject='New Service Request',
 
                message=f'''
New request submitted.
 
Name: {saved_request.full_name}
 
Email: {saved_request.email}
 
Phone: {saved_request.phone}
''',
 
                from_email=settings.EMAIL_HOST_USER,
 
                recipient_list=[
                    'rk.aulakhacc96@gmail.com'
                ],
 
                fail_silently=False,
            )
 
            # EMAIL TO USER
 
            send_mail(
 
                subject='Your Service Request Has Been Submitted',
 
                message=f'''
Hello {saved_request.full_name},
 
Your request has been submitted successfully.
 
Please contact on WhatsApp to complete payment and verification process.
 
Thank you.
''',
 
                from_email=settings.EMAIL_HOST_USER,
 
                recipient_list=[
                    saved_request.email
                ],
 
                fail_silently=False,
            )
 
            return redirect('success')
 
    else:
 
        form = form_class()
 
    return render(
        request,
        template_name,
        {'form': form}
    )
 
 
# =========================
# ITR REQUEST
# =========================
 
def itr_request(request):
 
    return handle_form(
        request,
        ITRRequestForm,
        'itr_form.html'
    )
 
 
# =========================
# GST REQUEST
# =========================
 
def gst_request(request):
 
    return handle_form(
        request,
        GSTRequestForm,
        'gst_form.html'
    )
 
 
# =========================
# TDS REQUEST
# =========================
 
def tds_request(request):
 
    return handle_form(
        request,
        TDSRequestForm,
        'tds_form.html'
    )
 
 
# =========================
# BOOKKEEPING REQUEST
# =========================
 
def bookkeeping_request(request):
 
    return handle_form(
        request,
        BookkeepingRequestForm,
        'bookkeeping_form.html'
    )