from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, EntrySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Entry
from .pagination import EntryPagination

from django.http import JsonResponse
from random import choice

from .titles_and_placeholders import titles_and_placeholders


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class EntryListCreate(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = EntryPagination
    
    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class EntryDelete(generics.DestroyAPIView): # TODO: перенос в корзину
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(author=user)
    
class EntriesSearch(generics.ListAPIView):
    serializer_class = EntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get("query")
        print(query)
        return Entry.objects.filter(author=user, content__contains=query)

def get_personalized_entry_hints(request):
    random_pair = choice(titles_and_placeholders)
    return JsonResponse({"title": random_pair[0], "placeholder": random_pair[1]})