from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic


class BookView(generic.ListView):
    template_name = 'books.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()

# def books_view(request):
#     book_value = models.Book.objects.all()
#     return render(request, "books.html",{"book_key":book_value})

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
       book = self.kwargs.get('id')
       return get_object_or_404(models.Book, id=book)

# def book_detail_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     return render(request, 'book_detail.html', {'book_key': book_id})

class CreateBookPostView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookPostView, self).form_valid(form=form)

# def createBookPostView(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Successfully was added!')
#     else:
#         form = forms.BookForm()
#     return render(request, 'create_book.html', {'form': form})

class UpdateBookPostView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = forms.BookForm
    success_url = '/'

    def get_object(self, **kwargs):
        book = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book)

    def form_valid(self, form):
        return super(UpdateBookPostView, self).form_valid(form=form)

class BookDropView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

def createBookView(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>The comment was successfully added!</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'create_review.html', {'form': form})

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

# def book_delete_view(request):
#     book_value = models.Book.objects.all()
#     return render(request, 'book_list.html', {'book_key': book_value})
#
# def book_drop_view(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return HttpResponse('Successfully was deleted!')


