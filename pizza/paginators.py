from rest_framework.pagination import PageNumberPagination

class TopSetPagination(PageNumberPagination):
    page_size = 10