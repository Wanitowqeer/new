from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .serializers import MusicianSerializer, AlbumSerializer
from .models import Musician, Album


class MusicianListView(APIView):
    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        data = serializer.data

        for musician in data:
            albums = Album.objects.filter(artist=musician['id'])
            serializer = AlbumSerializer(albums, many=True)
            musician['albums'] = serializer.data

        return Response(data)
    
    def post(self, request):
        serializer=MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

class MusicianDetailView(APIView):
    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)
    
    def put(self,request, pk, format=None):
        musician=self.get_object(pk)
        serializer = MusicianSerializer(musician,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        musician=self.get_object(pk)
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AlbumListView(APIView):
    def get(self,request):
        album=Album.objects.all()
        serializer=AlbumSerializer(album,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class AlbumdetailView(APIView):
    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        album = self.get_object(pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    def put(self,request, pk, format=None):
        album=self.get_object(pk)
        serializer = AlbumSerializer(album,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        album=self.get_object(pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)