from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from A_API.models import Comment




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']


