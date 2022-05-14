from django.contrib import admin
from django.urls import path
from main.views import index, blog, posting, new_post, remove_post   #from .views import * //이러면 공부가 안됨
from . import views

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

#path 함수 공부
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('',index),  #path('', index, name='index'),           !!!공부!!!! name='index' 파라미터
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'), #path('blog/',blog),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',posting, name="posting"),
	#user가 새로운 게시글(post)을 만드는 페이지
	path('blog/new_post/', new_post),
	#user가 게시글(post)을 삭제하는 페이지
	path('blog/<int:pk>/remove/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
