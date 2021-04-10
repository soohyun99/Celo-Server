from rest_framework import filters
from django.http import Http404
from django_filters.rest_framework import FilterSet, filters
from server.models import *

class ProduceFilter(FilterSet):
    id = filters.CharFilter(method='id_filter')
#    pw = filters.CharFilter(method='pw_filter')

    def id_filter(self, queryset, id, pw):
        id = self.request.query_params.get(id)
        pw = self.request.query_params.get(pw)
        if id is None:
            return 0
        elif id is not None:
            queryset = queryset.filter()
            if queryset.pw == pw :
                return 1
            else :
                return 0

#    def pw_filter(self, queryset, pw, value):
#        pw = self.request.query_params.get(pw, value)
#        if pw is None:
#            return 0
#        elif pw is not None:
#           queryset = queryset.filter(pw__icontains=value)
#            return 1