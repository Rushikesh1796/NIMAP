from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import clients
from .models import projects
from .serializers import clientsSerializer
from .serializers import projectsSerializer



# Create your views here.
class clientsList(APIView):

    def get(self,request):
        clients1=clients.objects.all()
        serializer=clientsSerializer(clients1, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializerobj=clientsSerializer(data=request.data)
        if serializerobj.is_valid():
            serializerobj.save()
            return Response(serializerobj.data,status=status.HTTP_201_CREATED)
        return Response(serializerobj.errors,status=status.HTTP_400_BAD_REQUEST) 

class clientsUpdatedel(APIView):

    def get_object(self,pk):
        try:
            return clients.objects.get(pk=pk)
        except clients.DoesNotExist:  
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        clientsobj=self.get_object(pk)
        serializerobj=clientsSerializer(clientsobj)
        return Response(serializerobj.data)

    def put(self,request,pk):
        clientsobj=self.getobject(pk)
        serializerobj=clientsSerializer(clientsobj,data=request.data)
        if serializerobj.is_valid():
            serializerobj.save()
            return Response(serializerobj.data,status=status.HTTP_200_OK)
        return Response(serializerobj.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        clientsobj=self.get_object(pk)
        clientsobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Projects Update Model:
class projectsList(APIView):

    def get(self,request):
        projects1=projects.objects.all()
        serializer=projectsSerializer(projects1, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializerobj=projectsSerializer(data=request.data)
        if serializerobj.is_valid():
            serializerobj.save()
            return Response(serializerobj.data,status=status.HTTP_201_CREATED)
        return Response(serializerobj.errors,status=status.HTTP_400_BAD_REQUEST) 



class projectsUpdatedel(APIView):
    def get_object(self,pk):
        try:
            return projects.objects.get(pk=pk)
        except projects.DoesNotExist:  
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        projectsobj=self.get_object(pk)
        serializerobj=projectsSerializer(projectsobj)
        return Response(serializerobj.data)

    def put(self,request,pk):
        projectsobj=self.getobject(pk)
        serializerobj=projectsSerializer(projectsobj,data=request.data)
        if serializerobj.is_valid():
            serializerobj.save()
            return Response(serializerobj.data,status=status.HTTP_200_OK)
        return Response(serializerobj.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        projectsobj=self.get_object(pk)
        projectsobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)