from django.views.generic import DetailView, ListView
from .models import Hrac, Tym, Liga, Zapas


class HracListView(ListView):
    model = Hrac
    template_name = 'hrac/hrac_list.html'
    context_object_name = 'hrac'


class HracDetailView(DetailView):
    model = Hrac
    template_name = 'hrac/hrac_detail.html'
    context_object_name = 'hrac'


class TymListView(ListView):
    model = Tym
    template_name = 'tym/tym_list.html'
    context_object_name = 'tym'


class TymDetailView(DetailView):
    model = Tym
    template_name = 'tym/tym_detail.html'
    context_object_name = 'tym'


class LigaListView(ListView):
    model = Liga
    template_name = 'liga/liga_list.html'
    context_object_name = 'liga'


class LigaDetailView(DetailView):
    model = Liga
    template_name = 'liga/liga_detail.html'
    context_object_name = 'liga'


class ZapasListView(ListView):
    model = Zapas
    template_name = 'zapas/zapas_list.html'
    context_object_name = 'zapas'


class ZapasDetailView(DetailView):
    model = Zapas
    template_name = 'zapas/zapas_detail.html'
    context_object_name = 'zapas'
