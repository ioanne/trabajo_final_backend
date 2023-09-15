from django.urls import path

from apps.character.views import CharacterTemplateView

urlpatterns = [path("", CharacterTemplateView.as_view(), name="character")]
