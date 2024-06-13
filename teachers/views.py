from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from  users.permissionmixin import TeacherRequiredMixin
from  django.views import  View
from  users.models import Teacher,Student,User
from  students.models import Lesson,Team
from users.forms import ProfileForm,ResetPasswordForm

class TeacherView(TeacherRequiredMixin,View):
    def get(self,request):
        return render(request,'teachers/dashboard.html')

class TeacherTimesView(TeacherRequiredMixin,View):
    def get(self,request):
        teacher = get_object_or_404(Teacher,user=request.user)
        teams = teacher.teacher.all()
        return render(request,'teachers/guruhlarim.html',{"teams":teams})

class TeacherGroup(TeacherRequiredMixin,View):
    def get(self,request,team_id):
        team = get_object_or_404(Team,id=team_id)
        lessons = team.lesson.all()
        return render(request,'teachers/guruh.html',{'team':team,'lessons':lessons})

class TeacherHomeworks(TeacherRequiredMixin,View):
    def get(self,request,team_id):
        team = get_object_or_404(Team,id=team_id)
        lessons = team.homeworks.all()
        return render(request,'teachers/guruh.html',{'team':team,'lessons':lessons})

class TeacherStudentsView(TeacherRequiredMixin,View):
    def get(self,request,team_id):
        team = get_object_or_404(Team,id=team_id)
        student = team.students.all()
        return render(request,'teachers/student.html',{'team':team,'student':student})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'teachers/profil.html',context={"user":user})

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'teachers/edit.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('teachers/dashboard')
        return render(request, 'teachers/edit.html', {'form': form})

class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'teachers/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('/')
        form = ResetPasswordForm()
        return render(request, 'teachers/reset_password.html', {'form':form})