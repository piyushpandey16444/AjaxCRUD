from django.shortcuts import render, get_list_or_404
from .forms import User
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home_view(request):
    form = UserForm()
    user_objs = get_list_or_404(User)
    context = {'form': form, 'users': user_objs}
    return render(request, 'enroll/home.html', context=context)


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')
            user = User(name=name, email=email, password=password)
            user.save()
            user_objs = get_list_or_404(User)
            return JsonResponse(data={'msg': 'User Created !', 'user_objs': user_objs})
        return JsonResponse(data=form.errors)
