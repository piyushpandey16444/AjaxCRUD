from django.shortcuts import render, get_list_or_404
from .forms import User
from .forms import UserForm
from django.http import JsonResponse


def home_view(request):
    form = UserForm()
    user_objs = get_list_or_404(User)
    context = {'form': form, 'users': user_objs}
    return render(request, 'enroll/home.html', context=context)


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = User(name=name, email=email, password=password)
            user.save()
            return JsonResponse(data={'response': 'User Created !'})
        return JsonResponse(data=form.errors)
