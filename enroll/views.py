from django.shortcuts import render, get_list_or_404
from .forms import User
from .forms import UserForm


def home_view(request):
    form = UserForm()
    user_objs = get_list_or_404(User)
    context = {'form': form, 'users': user_objs}
    return render(request, 'enroll/home.html', context=context)
