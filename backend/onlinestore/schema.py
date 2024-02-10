import graphene

from graphene_django.types import DjangoObjectType, ObjectType
from .models import CallBack


# Create a GraphQL type for the callback model
class CallBackType(DjangoObjectType):
    class Meta:
        model = CallBack
        fields = '__all__'


# Create a Query type
class Query(ObjectType):
    callback = graphene.Field(CallBackType, id=graphene.Int())
    callbacks = graphene.List(CallBackType)

    def resolve_callback(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return CallBack.objects.filter(pk=id).first()
        return None

    def resolve_callbacks(self, info, **kwargs):
        return CallBack.objects.all()


# Create Input Object Types
class CallBackInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    phone = graphene.String()


# Create mutations for callbacks
class CreateCallBack(graphene.Mutation):
    class Arguments:
        input = CallBackInput(required=True)

    status = graphene.Boolean()
    callback = graphene.Field(CallBackType)

    @staticmethod
    def mutate(root, info, input=None):
        status = True
        callback_instance = CallBack(name=input.name, phone=input.phone)
        callback_instance.save()
        return CreateCallBack(status=status, callback=callback_instance)


class Mutation(graphene.ObjectType):
    create_callback = CreateCallBack.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)