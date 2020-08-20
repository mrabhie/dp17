from django.urls import path
from dp17app import views
app_name="dp17app"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multiplesel,name="multiselect"),
    path('img/',views.imgupld,name="img"),
    path('imgdis/',views.imgdis,name="img_disp"),
    path('builtin/',views.builtin,name="builtin"),
]