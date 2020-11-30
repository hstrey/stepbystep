from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
import json
from bokeh.plotting import figure
from bokeh.embed import components
import numpy as np

# Create your views here.

from .models import Gaitdata

class GaitListView(ListView):
    model = Gaitdata
    template_name = 'gait/gait_list.html'
    context_object_name = 'all_gaitdata_list'

    def get_queryset(self):
        queryset = super(GaitListView, self).get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset

def gaitGraphView(request,pk):
    if request.user.is_authenticated:
        data = get_object_or_404(Gaitdata, pk=pk)
        data_dict = json.loads(data.data_json)
        data_list = data_dict['data']
        t_data = np.arange(len(data_list))/200.0
        plot = figure(title=str(data.created_date),x_axis_label='time')
        plot.line(t_data,data_list)
        script, div = components(plot)
        context = {'script': script,'div':div}
    else:
        context = {'script':"","div":""}
    return render(request, 'gait/gait_graph.html', context)
