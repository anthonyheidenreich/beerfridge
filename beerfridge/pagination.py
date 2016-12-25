from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param, remove_query_param

class Pagination(PageNumberPagination):
    page_size = 20
    max_page_size = 20
    ordering = 'id'
