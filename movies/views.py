from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from movies.models import MoviesData, MoviesGenre
from movies.serializers import MoviesDataSerializer, MoviesGenreSerializer

class MoviesList(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    """
    List all movies, or create a new movies.
    """
    def get(self, request, format=None):
        print "Moviessssss list"
        movies = MoviesData.objects.all()
        serializer = MoviesDataSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        my_file = request.FILES['moviepic']
        filename = '/tmp/myfile'
        with open(filename, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)

        my_saved_file = open(filename) #there you go


        print "Create movies",request.data
        serializer = MoviesDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MoviesDetail(APIView):
    
    """
    Retrieve, update or delete a Movies instance.
    """
    def get_object(self, pk):
        try:
            return MoviesData.objects.get(pk=pk)
        except MoviesData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MoviesDataSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):        

        movie = self.get_object(pk)
        serializer = MoviesDataSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GenreList(APIView):
    """
    List all genre, or create a new genre.
    """
    def get(self, request, format=None):
        movies_genre = MoviesGenre.objects.all()
        serializer = MoviesGenreSerializer(movies_genre, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MoviesGenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetails(APIView):
    """
    Retrieve, update or delete a Genre instance.
    """
    def get_object(self, pk):
        try:
            return MoviesGenre.objects.get(pk=pk)
        except MoviesGenre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie_genre = self.get_object(pk)
        serializer = MoviesGenreSerializer(movie_genre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie_genre = self.get_object(pk)
        serializer = MoviesGenreSerializer(movie_genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie_genre = self.get_object(pk)
        movie_genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)