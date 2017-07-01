from django.conf.urls import include, url


urlpatterns = [
    url(r'^',
        include('{{ project_name }}.apps.main.urls', namespace='main')),
]
