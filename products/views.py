from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_list_view(request):
    queryset = Product.objects.all()

    context = { "object_list": queryset, }

    return render(request, "products/product_list.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context ={ 'form': form }

    return render(request, "products/product_create.html", context)


def product_update_view(request, pk):
    obj = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('../')

    context = { 'form': form }

    return render(request, "products/product_edit.html", context)


def product_detail_view(request, pk):
    obj = get_object_or_404(Product, id=pk)
    context = { "object": obj }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, pk):
    obj = get_object_or_404(Product, id=pk)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    context = { 'object': obj, }

    return render(request, "products/product_delete.html", context)


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the form is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#             my_form = RawProductForm()
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, 'products/product_create.html', context)
