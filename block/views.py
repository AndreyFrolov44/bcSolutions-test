from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from .models import Block


class BlocksListView(ListView):
    model = Block
    paginate_by = 100
    context_object_name = 'blocks'
    template_name = 'block/index.html'


class BlockDetailView(DetailView):

    model = Block
    template_name='block/detail.html'

    def get_object(self):
        block = get_object_or_404(Block, height=self.kwargs['height'])
        return block
