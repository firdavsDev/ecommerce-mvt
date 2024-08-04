from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from accounts.forms.profile import ProfileForm
from accounts.models.profile import Profile


class ProfileView(View):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=profile)
        return render(request, "accounts/profile.html", {"form": form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        # accep image file also
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            messages.success(request, "Profile updated successfully.")
            form.save()
            return redirect("accounts:profile")
        return render(
            request, "accounts/profile.html", {"form": form, "instance": profile}
        )


profile_view = ProfileView.as_view()
