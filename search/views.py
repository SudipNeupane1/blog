from django.shortcuts import render

from articles.models import Article



SEARCH_TYPE_MAPPING = {
    'articles': Article,
    'artices':Article,
}

def search_view(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    Klass = Article
    if search_type in SEARCH_TYPE_MAPPING.keys():
        Klass = SEARCH_TYPE_MAPPING[search_type]
    qs = Klass.object.search(query=query)
    context = {
        'queryset':qs
    }
    template = "search/results.htm"
    if request.htmx:
        content['queryset'] = qs[:5]
        template = "search/partia"