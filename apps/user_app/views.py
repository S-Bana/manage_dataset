from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for users.
    Your API endpoints for user management will be available at:
    GET /api_user/: List all users.
    POST /api_user/: Create a new user.
    GET /api_user/{id}/: Retrieve a specific user by ID.
    PUT /api_user/{id}/: Update a specific user by ID.
    PATCH /api_user/{id}/: Partially update a specific user by ID.
    DELETE /api_user/{id}/: Delete a specific user by ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def perform_create(self, serializer):
        serializer.save()