from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Slider, Service, Doctor, Faq, Gallery
from django.views.generic import ListView, DetailView, TemplateView


class HomeView(ListView):
    template_name = 'hotel/index.html'
    queryset = Service.objects.all()
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['sliders'] = Slider.objects.all()
        context['experts'] = Doctor.objects.all()
        return context


class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = "hotel/services.html"


class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = "hotel/service_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.all()
        return context


class DoctorListView(ListView):
    template_name = 'hotel/team.html'
    queryset = Doctor.objects.all()
    paginate_by = 8


class DoctorDetailView(DetailView):
    template_name = 'hotel/team-details.html'
    queryset = Doctor.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctor.objects.all()
        return context


class FaqListView(ListView):
    template_name = 'hotel/faqs.html'
    queryset = Faq.objects.all()


class GalleryListView(ListView):
    template_name = 'hotel/gallery.html'
    queryset = Gallery.objects.all()
    paginate_by = 9


class ContactView(TemplateView):
    template_name = "hotel/contact.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "BitMasters Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+phone,
                message,
                email,
                ['dioufm65@yahoo.com'],
                fail_silently=False,
            )
            messages.success(request, " Email envoyez avec succes...")

        return redirect('contact')
