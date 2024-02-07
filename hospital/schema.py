import graphene
from graphene_django import  DjangoObjectType
from .models import Hospital

class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital
        fields = ('id','name','address','phone_number','email','website','capacity')

class Query(graphene.ObjectType):

    all_hospitals = graphene.List(HospitalType)

    def resolve_all_hospitals(self, info):
        return Hospital.objects.all()
    
schema = graphene.Schema(query=Query)