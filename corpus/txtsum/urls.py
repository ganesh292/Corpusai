from django.urls import path
from . import views

urlpatterns = [
    path('', views.features, name='features'),
    # path('image', views.image, name='image'),
    path('camera', views.camera, name='camera'),
    path('sumtext', views.sumtext, name='sumtext'),
    path('urltext', views.url2text, name='urltext'),
    path('doc2text', views.doc2text, name='doc2text'),
    path('qna', views.qna, name='qna'),
    path('chatbot', views.chatbot, name='chatbot'),
    
]