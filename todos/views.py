from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        # Get the search query parameter
        search_query = request.GET.get('search', '')

        # Filter todos by title if search_query is provided
        if search_query:
            todos = Todo.objects.filter(title__icontains=search_query)
            if not todos.exists():  # Check if the queryset is empty
                return Response({'error': 'No todos found matching the search query.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            todos = Todo.objects.all()
        if not todos.exists():
            return Response({'empty_list': 'Your list is empty.'}, status=status.HTTP_200_OK)
    
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        # Ensure 'completed' is a boolean value (either True or False)
        completed = request.data.get('completed')
        if completed is not None and not isinstance(completed, bool):
            return Response({'error': "'completed' must be a boolean value (true or false)."}, status=status.HTTP_400_BAD_REQUEST)
     
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'completed': False,  # Default value
        }

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def todo_detail(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Todo with the specified ID does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'  # Determine if it's a partial update
      
        completed = request.data.get('completed')
               # Validate 'completed' if it's provided in the request
        if completed is not None and not isinstance(completed, bool):
            return Response({'error': "'completed' must be a boolean value (true or false)."}, status=status.HTTP_400_BAD_REQUEST)
      
        serializer = TodoSerializer(todo, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'Todo has been deleted.'}, status=status.HTTP_204_NO_CONTENT)