from django.views.generic import TemplateView

class HomePageview(TemplateView):
    template_name = 'home.html'