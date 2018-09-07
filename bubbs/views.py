import json

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from bubbs.models import BidKeyGenerator

# Create your views here.


class Bid(object):
    class Generate(View):
        def get(self, request, n=1):
            return HttpResponse(json.dumps([BidKeyGenerator.generate() for _ in range(n)]))

