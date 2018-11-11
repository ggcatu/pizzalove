from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import F
from rest_framework import generics, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .forms import CustomUserCreationForm
from .models import CustomUser
from .serializers import CustomUserSerializer
from .paginators import TopSetPagination
from .permissions import SamePk


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@api_view(['GET'])
@permission_classes((IsAuthenticated, SamePk))
def LoveItView(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user.pizza_love = F('pizza_love') + 1
    user.save()
    user.refresh_from_db()
    return Response({"loveit": user.pizza_love})

class ListUsersView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    renderer_classes = (JSONRenderer, )
    serializer_class = CustomUserSerializer
    pagination_class = TopSetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pizza_love',)
    ordering = '-pizza_love'