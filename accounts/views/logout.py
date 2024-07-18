# logout view
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("store:store_list")


logout_view = LogoutView.as_view()
