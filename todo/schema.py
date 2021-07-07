import graphene
from graphene_django import DjangoObjectType
# import Todo Model in our schema
from .models import Todo, Like
# import User Model for CreateLike
from user.schema import UserType
# Q object for complex queries
from django.db.models import Q


class TodoType(DjangoObjectType):
    # initialize Todo Object Type
    class Meta:
        model = Todo


class LikeType(DjangoObjectType):
    # initialize Like Object Type
    class Meta:
        model = Like


class Query(graphene.ObjectType):
    # create todo query type
    todo_field = graphene.List(TodoType, search=graphene.String())
    like_field = graphene.List(LikeType)

    def resolve_todo_field(self, info, search=None):
        if search:
            filter = (
                Q(title__icontains=search) |
                Q(posted_by__username__icontains=search)
            )
            return Todo.objects.filter(filter)
        # list all todo
        return Todo.objects.all()

    def resolve_like_field(self, info):
        # list all likes
        return Like.objects.all()


class CreateTodo(graphene.Mutation):
    todo_field = graphene.Field(TodoType)

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        url = graphene.String()
        completed = graphene.Boolean()

    # we can use **kwargs pattern
    def mutate(self, info, title, description, url, completed):
        # get information from user
        user_data = info.context.user  # or None

        # raise Exception when anonymous
        if user_data.is_anonymous:
            raise Exception('Login required')

        todo_data = Todo(title=title,
                         description=description,
                         url=url,
                         completed=completed,
                         posted_by=user_data)
        todo_data.save()
        return CreateTodo(todo_field=todo_data)


class UpdateTodo(graphene.Mutation):
    todo_field = graphene.Field(TodoType)

    class Arguments:
        todo_id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        completed = graphene.Boolean()
        url = graphene.String()

    def mutate(self, info, todo_id, title, description, url, completed):
        user_data = info.context.user
        todo_data = Todo.objects.get(id=todo_id)

        # raise Exception when anonymous
        if todo_data.posted_by != user_data:
            raise Exception('Not permitted to update')

        todo_data.title = title
        todo_data.description = description
        todo_data.url = url
        todo_data.completed = completed

        todo_data.save()
        return UpdateTodo(todo_field=todo_data)


class DeleteTodo(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        todo_id = graphene.Int(required=True)

    def mutate(self, info, todo_id):
        user_data = info.context.user
        todo_data = Todo.objects.get(id=todo_id)

        # raise Exception when anonymous
        if todo_data.posted_by != user_data:
            raise Exception('Not permitted to delete')

        todo_data.delete()
        return DeleteTodo(message="Todo deleted")


class CreateLike(graphene.Mutation):
    user_field = graphene.Field(UserType)
    todo_field = graphene.Field(TodoType)

    class Arguments:
        todo_id = graphene.Int(required=True)

    def mutate(self, info, todo_id):
        user_data = info.context.user

        if user_data.is_anonymous:
            raise Exception('Login required')

        user_data = info.context.user
        todo_data = Todo.objects.get(id=todo_id)

        if not todo_data:
            raise Exception('Todo not found')

        Like.objects.create(
            user_field=user_data,
            todo_field=todo_data
        )
        return CreateLike(user_field=user_data, todo_field=todo_data)


class DeleteLike(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        todo_id = graphene.Int(required=True)

    def mutate(self, info, todo_id):
        user_data = info.context.user
        todo_data = Todo.objects.get(id=todo_id)

        if todo_data.posted_by != user_data:
            raise Exception('Not permitted to unlike')

        Like.objects.filter(
            user_field=user_data,
            todo_field=todo_data
        ).delete()
        return DeleteLike(message="Like deleted")


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
    create_like = CreateLike.Field()
    delete_like = DeleteLike.Field()
