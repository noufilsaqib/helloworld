from django.urls import path
from .views import homePageView, aboutPageView, noufilPageView, homePost, results

urlpatterns = [
    path("", homePageView, name="home"),
    path("about/", aboutPageView, name="about"),
    path("noufil/", noufilPageView, name="noufil"),
    path("homePost/", homePost, name="homePost"),
    path("results/<int:choice>/<str:gmat>/", results, name="results"),
]
