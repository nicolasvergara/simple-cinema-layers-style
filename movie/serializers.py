from rest_framework import serializers

from movie import models


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = ('__all__')