from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from topic_list.models import TopicList
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView

class TopicListListView(ListView):
    
    model = TopicList

class TopicListCreateView(CreateView):
    
    model = TopicList

    model = TopicList
    fields = ['presentation_date', 'topic', 'multi_person', 'note']
    success_url = '/'

class TopicListDetailView(DetailView):

    model = TopicList

class TopicListUpdateView(UpdateView):
    model = TopicList
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/'
  

class TopicListDeleteView(DeleteView):
    model = TopicList
    success_url = '/'
