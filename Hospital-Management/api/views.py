from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Doctors
from  .serializer import DoctorsSerializer

# Create your views here.
@api_view(["GET", "POST"])
def create_read(request):
    if request.method == 'GET':
        data = Doctors.objects.all()
        serialized_data = DoctorsSerializer(data, many = True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        deserialized_data = DoctorsSerializer(data = request.data)
        if deserialized_data.is_valid():
            deserialized_data.save()
            return Response(deserialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(deserialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def update_delete(request, did):
    try:
        record = Doctors.objects.get(id = did)
    except Doctors.DoesNotExist:
        return Response({"error":"ID does not exists..."}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data = Doctors.objects.filter(id = did)
        serialized_data = DoctorsSerializer(data, many = True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        update_data = DoctorsSerializer(record, data = request.data)
        if update_data.is_valid():
            update_data.save()
            return Response(update_data.data, status=status.HTTP_200_OK)
        else:
            return Response(update_data.error, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "PATCH":
        update_data = DoctorsSerializer(record, data = request.data, partial = True)
        if update_data.is_valid():
            update_data.save()
            return Response(update_data.data, status=status.HTTP_200_OK)
        else:
            return Response(update_data.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        record.delete()
        return Response({}, status=status.HTTP_200_OK)
