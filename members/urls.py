from django .urls import path
from members.views import  (UserRegistrationAPIView)


urlpatterns =[
    path('user/register', UserRegistrationAPIView.as_view())
    # path('test',JustATestView.as_view())
]