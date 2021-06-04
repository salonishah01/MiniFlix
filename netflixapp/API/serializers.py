from rest_framework import serializers
from netflixapp.models import Video, Catogorie

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # fields = ['name', 'img1', 'img2', 'img3', 'starring', 'creators', 'desc', 'year', 'category']
        fields = '__all__'

class VideoCategorie(serializers.ModelSerializer):
    video_category = VideoSerializer(many=True, read_only=True)
    class Meta:
        model = Catogorie
        fields = ['id', 'name', 'video_category']
        