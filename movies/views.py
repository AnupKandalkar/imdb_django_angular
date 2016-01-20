from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict

from movies.models import MoviesData, MoviesGenre
from movies.serializers import MoviesDataSerializer, MoviesGenreSerializer


# from rest_framework.authentication import SessionAuthentication 

# class CsrfExemptSessionAuthentication(SessionAuthentication):

#     def enforce_csrf(self, request):
#         return  # To not perform the csrf check previously happening


# authentication_classes = (CsrfExemptSessionAuthentication)

class MoviesList(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    """
    List all movies, or create a new movies.
    """
    def get(self, request, format=None):
        print "movie get method"
        movies = MoviesData.objects.all()
        serializer = MoviesDataSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print "movie post method"
       
        movie_data = MoviesData()
        movie_data.name = request.POST.get('name')
        movie_data.ssdb_score = int(request.POST.get('ssdb_score'))
        movie_data.popularity = int(request.POST.get('popularity'))
        movie_data.director = request.POST.get('director')
        movie_data.description = request.POST.get('description')
        movie_data.stars = request.POST.get('stars')
        movie_data.save()


        for genre_id in request.POST.getlist('genre[]'):
            movie_data.genre.add(int(genre_id))    
       
        dict_data = model_to_dict(movie_data)
        print "previous data",request.data
        print "dict data",dict_data
        # import pdb
        # pdb.set_trace()
        serializer = MoviesDataSerializer(data=dict_data)
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
        print "movie update get method"
        movie = self.get_object(pk)
        serializer = MoviesDataSerializer(movie)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):         
        movie = self.get_object(pk)
        genre_list = []
        movie_data = {}
        data = request.data
        movie_data = dict(data.iterlists())       
        genre_list = [int(genre_id) for genre_id in movie_data.get('genre[]')]
                
        movie_data['genre'] = genre_list
        movie_data['name'] = request.data['name']
        movie_data['director'] = request.data['director']
        movie_data['description'] = request.data['description']
        movie_data['stars'] = request.data['stars']
        movie_data['ssdb_score'] = int(request.data['ssdb_score'])
        movie_data['popularity'] = int(request.data['popularity'])

        movie_data['create_date'] = None
        
        serializer = MoviesDataSerializer(movie, data=movie_data)        
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
        print "Genre creation"
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