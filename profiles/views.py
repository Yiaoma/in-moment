from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profile/profile.html"
    context = {
        "form": form,
        "orders": orders,
    }

    return render(request, template, context)