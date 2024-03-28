from django.shortcuts import render
from myapp.models import CustomUser

def my_view(request):
    # Get the logged-in user's admin
    admin = request.user.admin

    # Filter users based on the admin
    users = CustomUser.objects.filter(admin=admin)

    context = {
        'users': users
    }

    return render(request, 'my_template.html', context)
