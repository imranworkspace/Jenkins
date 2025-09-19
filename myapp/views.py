from django.shortcuts import render
from .models import StudentModel
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    return render(request,'home.html')

@api_view(['GET'])
def viewall(request,pk=None):
    if pk is not None:
        try:
            stud_pk = StudentModel.objects.get(pk=pk)
        except StudentModel.DoesNotExist:
            return Response({'response':f'{pk} id does not exists'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serilizer = StudentSerializer(stud_pk)
            return Response({'response':serilizer.data},status=status.HTTP_200_OK)
    else:
        try:
            all = StudentModel.objects.all()
        except StudentModel.DoesNotExist:
            return Response({'response':'id does not exists'},status=status.HTTP_400_BAD_REQUEST)
        else:
            serilizer = StudentSerializer(all,many=True)
            return Response({'response':serilizer.data},status=status.HTTP_200_OK)

