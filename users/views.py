from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# Create your views here.
class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'