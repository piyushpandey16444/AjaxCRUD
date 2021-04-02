from django.shortcuts import render
from .forms import User
from .forms import UserForm


def home_view(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'enroll/home.html', context=context)
