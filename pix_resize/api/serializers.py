from rest_framework import serializers
from .models import Picture


class PixSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = '__all__'

    def create(self, validated_data):
        url = validated_data.get('url')
        picture = validated_data.get('picture')

        if url:
            picture = Picture.save_img_from_url(url)
            validated_data['picture'] = picture

        return Picture.objects.create(**validated_data)
