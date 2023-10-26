from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view),
    path('book_detail/<int:id>/', views.book_detail_view),
    # <спецификатор:название_параметра>
    path('book_list/', views.book_delete_view),
    path('book_list/<int:id>/delete/', views.book_drop_view),
    path('create_post_book/', views.createBookPostView),
    path('add_comment/', views.createBookView),
]
