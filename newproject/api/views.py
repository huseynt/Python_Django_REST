from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer(
        {
        'name': 'John', 
        'age': 30, 
        'email':4141, 
        'json': {'key': 'value'}
         }
        ).data, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
def post_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        testData = serializer
        testData={
            "response": "success",
        }
        return Response(testData, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# post data
# {
#     "age": 30,
#     "name": "John",
#     "email": "hus@mail.ru",
#     "json": {
#         "key": "value"
#     }
# }