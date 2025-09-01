from django.urls import path
from . import views

urlpatterns = [
    path('diary', views.EntryListCreate.as_view(), name='diary'),
    path('diary/delete/<int:pk>', views.EntryDelete.as_view(), name='delete-entry'), # TODO: uuid
    path('diary/search/', views.EntriesSearch.as_view(), name='search-entries'),
    path('entry-hints', views.get_personalized_entry_hints, name='entry-hints'),
]