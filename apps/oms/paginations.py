from rest_framework.pagination import PageNumberPagination


class MyPageNumberPaginations(PageNumberPagination):
    '''
    settings.py里面看看有没有做全局变量，
    但是因为这里的等级比全局变量高，所以一般会以这个文件来显示。
    '''
    page_size = 15  # 默认15行/页
    max_page_size = 50  # 最大50行/页
    page_query_param = 'page'
    page_size_query_param = 'size'
