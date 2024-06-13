from django.urls import path
from .views import  TeacherView,TeacherTimesView,TeacherGroup,TeacherHomeworks,TeacherStudentsView,ProfileView,EditProfileView,ResetPasswordView,TeacherCreateLessonView,TeacherStudentLeson

app_name = 'teachers'


urlpatterns = [
    path('dashboard/',TeacherView.as_view(),name='dashboard'),
    path('guruhlarim/',TeacherTimesView.as_view(),name='guruhlarim'),
    path('resed_password/',ResetPasswordView.as_view(),name='resed_password'),
    path('profil-teacher/',ProfileView.as_view(),name='profil'),
    path('guruh/<int:team_id>/',TeacherGroup.as_view(),name='guruh'),
    path('homework/<int:team_id>/',TeacherHomeworks.as_view(),name='homeworks'),
    path('edit/<int:id>/',EditProfileView.as_view(),name='edit'),
    path('student/<int:team_id>/',TeacherStudentsView.as_view(),name='student'),
    path('create/<int:team_id>/',TeacherCreateLessonView.as_view(),name='create'),
    path('stydents/<int:id>/',TeacherStudentLeson.as_view(),name='stydents'),
]