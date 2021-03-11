from django.conf.urls import url, include
from django.urls import path, include
from graphene_django.views import GraphQLView


urlpatterns = [
    path("", GraphQLView.as_view(graphiql=True)),
]
