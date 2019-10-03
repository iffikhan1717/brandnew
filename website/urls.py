from django.urls import path
from .views import homeview,tajikabad,ms,jinnah,ms_heights,aboutus,latest_project,posts,sig_post,contact_us
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('', homeview, name='homepage'),
    path('aghajee-apart', tajikabad, name='tj'),
    path('jinnah-apartment', jinnah, name='jin'),
    path('Aghajee-malik-saleem ', ms, name='ms'),
    path('Aghajee-malik-saleem-height ', ms_heights, name='msh'),
    path('latest-projects ', latest_project, name='lstt'),
    path('about-us', aboutus, name='abt'),
    path('contact-us', contact_us, name='cont-us'),
    path('blog', posts , name='psts'),
    path('<int:pos_id>', sig_post, name='sigpst'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
