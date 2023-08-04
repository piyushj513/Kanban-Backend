from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User,Card,Comments,Col,Board
from .serializers import UserSerializer, BoardSerializer, ColSerializer, CardSerializer, CommentsSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# Create your views here.

class CRUDAPI(APIView):
    model = None
    serializer_class = None

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None

    def get(self, request, pk=None):
        if pk is None:
            objects = self.model.objects.all()
            serializer = self.serializer_class(objects, many=True)
            return Response(serializer.data)
        else:
            obj = self.get_object(pk)
            if not obj:
                return Response(f"{self.model.__name__} not found", status=status.HTTP_404_NOT_FOUND)

            serializer = self.serializer_class(obj)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(f"{self.model.__name__} not found", status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(f"{self.model.__name__} not found", status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response(f"{self.model.__name__} Deleted Successfully", status=status.HTTP_204_NO_CONTENT)

class UserListAPIView(CRUDAPI):
    model = User
    serializer_class = UserSerializer
    
class CardListAPIView(CRUDAPI):
    model = Card
    serializer_class = CardSerializer

class UserLoginAPIView(APIView):   
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response("Invalid email or password", status=status.HTTP_400_BAD_REQUEST)
        result=check_password(password,user.password)
        if(result):
            data = {
                'name': user.first_name,
                'message': 'Login successful',
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response("Invalid email or password", status=status.HTTP_400_BAD_REQUEST)

    
class UserRegistration(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
 
        try:
            user = User.objects.get(email=email)
            return Response("Username already exists", status=status.HTTP_409_CONFLICT)
        except User.DoesNotExist:
            hashed_password = make_password(password)
            user = User.objects.create(email=email, password=hashed_password, first_name=first_name,last_name=last_name)
            user.save()
            data = {
                'email': user.email,
                'message': 'Registration successful',
            }
            return Response(data, status=status.HTTP_201_CREATED)

class CommentsListAPIView(CRUDAPI):
    model = Comments
    serializer_class = CommentsSerializer

# class CardListAPIView(APIView):
#     def get(self, request):
#         cards = Card.objects.all()
#         serializer = CardSerializer(cards, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = CardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CardListAPIView2(APIView):
#     def put(self, request,pk):
#         try:
#             cards = Card.objects.get(card_id=pk)
#         except Card.DoesNotExist:
#             return Response("Card not found", status=status.HTTP_404_NOT_FOUND)
        
#         serializer = CardSerializer(cards,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, pk):
#         cards = Card.objects.get(card_id=pk)
#         cards.delete()
#         return Response("Card Deleted Successfully", status=status.HTTP_201_CREATED)
    

# class BoardListAPIView(APIView):
#     def get(self, request):
#         boards = Board.objects.all()
#         serializer = BoardSerializer(boards, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = BoardSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BoardListAPIView2(APIView):
#     def put(self, request,pk):
#         boards = Board.objects.get(board_id=pk)
#         serializer = BoardSerializer(boards,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, pk):
#         boards = Board.objects.get(user_id=pk)
#         boards.delete()
#         return Response("Board Deleted Successfully", status=status.HTTP_201_CREATED)

# class ColListAPIView(APIView):
#     def get(self, request):
#         cols = Col.objects.all()
#         serializer = ColSerializer(cols, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ColSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class ColListAPIView2(APIView):
#     def put(self, request,pk):
#         cols = Col.objects.get(col_id=pk)
#         serializer = ColSerializer(cols,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, pk):
#         cols = Col.objects.get(col_id=pk)
#         cols.delete()
#         return Response("Column Deleted Successfully", status=status.HTTP_201_CREATED)


    
# class CommentsListAPIView(APIView):
#     def get(self, request):
#         comments = Comments.objects.all()
#         serializer = CommentsSerializer(comments, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CommentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class CommentsListAPIView2(APIView):
#     def put(self, request,pk):
#         com = Comments.objects.get(comment_id=pk)
#         serializer = CommentsSerializer(com,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request, pk):
#         coms = Comments.objects.get(comment_id=pk)
#         coms.delete()
#         return Response("Column Deleted Successfully", status=status.HTTP_201_CREATED)
