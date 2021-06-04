from rest_framework import viewsets
from .serializers import VideoSerializer, VideoCategorie
from netflixapp.models import Video, Catogorie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class VideoList(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', 'starring', 'year']
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class videocategorylist(viewsets.ModelViewSet):
    queryset = Catogorie.objects.all()
    serializer_class = VideoCategorie