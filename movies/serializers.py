from rest_framework import serializers
from movies.models import MoviesData, MoviesGenre


class MoviesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesData

class MoviesGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesGenre        