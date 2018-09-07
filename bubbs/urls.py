from django.urls import path
from django.views.generic import TemplateView

from bubbs.views import Bid

urlpatterns = [
    path('', TemplateView.as_view(template_name='bubbs/home.html')),
    path('bid/', TemplateView.as_view(template_name='bubbs/bid.html'), name='bid'),

    path('bid/generate/', Bid.Generate.as_view()),
    path('bid/generate/<int:n>/', Bid.Generate.as_view())
]