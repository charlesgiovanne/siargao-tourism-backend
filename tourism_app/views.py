from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .models import Explore, Search
from .serializers import UserSerializer, ExploreSerializer, SearchSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = get_user_model().objects.filter(email=email).first()
        if user and user.check_password(password):
            if not user.is_verified:
                return Response({'error': 'Email not verified'}, status=status.HTTP_403_FORBIDDEN)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def forgot_password(self, request):
        email = request.data.get('email')
        user = get_user_model().objects.filter(email=email).first()
        if user:
            user.generate_reset_token()
            return Response({'message': 'Reset link sent to email'})
        return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def verify_email(self, request):
        token = request.data.get('token')
        user = get_user_model().objects.filter(verification_token=token).first()
        if user:
            user.is_verified = True
            user.verification_token = None
            user.save()
            return Response({'message': 'Email verified successfully'})
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        return Response({'message': 'Logout successful'})

class ExploreViewSet(viewsets.ModelViewSet):
    queryset = Explore.objects.all()
    serializer_class = ExploreSerializer
    permission_classes = [AllowAny]

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
