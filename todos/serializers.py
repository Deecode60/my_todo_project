from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created_at']

    # Adding validation to ensure 'title' is required and within max length
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required.")
        if len(value) > 255:
            raise serializers.ValidationError("Title cannot be more than 255 characters.")
        return value

    # Validate 'completed' field (should be a boolean value)
    def validate_completed(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("Completed must be a boolean value (True or False).")
        return value
