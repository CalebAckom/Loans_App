import graphene
from graphene_django.types import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()


class CreateUser(graphene.Mutation):
    class Arguments:
        phone_number = graphene.String()
        password = graphene.String()

    user = graphene.Field(UserType)

    def mutate(self, info, phone_number, password):
        user = User.objects.create_user(phone_number=phone_number, password=password)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
