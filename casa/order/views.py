from ast import arg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import *
from django.http import  HttpResponseRedirect
# Create your views here.

class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy('product:product-list')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    
    def get_success_url(self):
        return reverse_lazy('product:product-detail', args=[self.object.id])
    

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product-list')
    template_name ='order/properties_confirm_delete.html'

    def form_valid(self, form):
        self.object = self.get_object()
        success_url = self.get_success_url()
        deleted_product = Product( pk = self.object.id,
                                    product_name = self.object.product_name,
                                    collection = self.object.collection,
                                    surface = self.object.surface,
                                    weight = self.object.weight,
                                    thickness = self.object.thickness,
                                    size = self.object.size,
                                    product_image = self.object.product_image,
                                    preview =self.object.preview,
                                    is_deleted = True,
                                    product_quantity = self.object.product_quantity

                                    )
        deleted_product.save()
        return HttpResponseRedirect(success_url)


# ------------------------------------Size---------------------------------------------------

class SizeCreateView(CreateView):
    model = Size
    fields = "__all__"
    success_url = reverse_lazy('product:size-list')
    template_name = 'order/product_properties_form.html'
    

class  SizeListView(ListView):
    model = Size
    template_name = 'order/product_properties_list.html'

class SizeDetailView(DetailView):
    model = Size
    template_name = 'order/product_properties_detail.html'

class SizeUpdateView(UpdateView):
    model = Size
    fields = "__all__"
    template_name = 'order/product_properties_form.html'

    def get_success_url(self):
        return reverse_lazy('product:size-detail', args=[self.object.id])
    

class SizeDeleteView(DeleteView):
    model = Size
    success_url = reverse_lazy('product:size-list')
    template_name = 'order/properties_confirm_delete.html'
      


# ---------------------------------Thickness---------------------------------------------------


class ThicknessCreateView(CreateView):

    model = Thickness
    fields = "__all__"
    success_url = reverse_lazy('product:thickness-list')
    template_name = 'order/product_properties_form.html'


class ThicknessListView(ListView):
    model = Thickness
    template_name = 'order/product_properties_list.html'


class ThicknessDetailView(DetailView):
    model = Thickness
    template_name = 'order/product_properties_detail.html'

class ThicknessUpdateView(UpdateView):
    model = Thickness
    fields = "__all__"
    template_name = 'order/product_properties_form.html'

    def get_success_url(self):
        return reverse_lazy('product:thickness-detail', args=[self.object.id])
    
class ThicknessDeleteView(DeleteView):
    model = Thickness
    success_url = reverse_lazy('product:thickness-list')    
    template_name = 'order/properties_confirm_delete.html'






# ----------------------------------Surface--------------------------------------------------

class SurfaceCreateView(CreateView):
    model = Surface
    fields = "__all__"
    success_url = reverse_lazy('product:surface-list')
    template_name = 'order/product_properties_form.html'


class SurfaceListView(ListView):
    model = Surface
    template_name = 'order/product_properties_list.html'


class SurfaceDetailView(DetailView):
    model = Surface
    template_name = 'order/product_properties_detail.html'

class SurfaceUpdateView(UpdateView):
    model = Surface
    fields = "__all__"
    success_url = reverse_lazy('product:surface-detail')
    template_name = 'order/product_properties_form.html'

    def get_success_url(self):
        return reverse_lazy('product:surface-detail', args=[self.object.id])
    
    
class SurfaceDeleteView(DeleteView):
    model = Surface
    success_url = reverse_lazy('product:surface-list')
    template_name = 'order/properties_confirm_delete.html'


# --------------------------------Collection---------------------------------------------------


class CollectionCreateView(CreateView):
    model = Collection
    fields = "__all__"
    success_url = reverse_lazy('product:collection-list')
    template_name = 'order/product_properties_form.html'
    


class CollectionListView(ListView):
    model = Collection
    template_name = 'order/product_properties_list.html'


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'order/product_properties_detail.html'

class CollectionUpdateView(UpdateView):
    model = Collection
    fields = "__all__"
    template_name = 'order/product_properties_form.html'
    

    def get_success_url(self):
        return reverse_lazy('product:collection-detail', args=[self.object.id])
    
    
class CollectionDeleteView(DeleteView):
    model = Collection
    success_url = reverse_lazy('product:collection-list') 
    template_name = 'order/properties_confirm_delete.html'