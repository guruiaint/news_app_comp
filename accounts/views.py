from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("article_list")
    template_name = "registration/signup.html"