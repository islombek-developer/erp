from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm,ProfileForm,StudentEditForm,ResetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User,Student,Team,Teacher
from .permissionmixin import AdminRequiredMixin,StudentRequiredMixin,TeacherRequiredMixin
from django.db.models import Q

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role=='student':
                    return redirect('students/dashboard')
                elif user.user_role=='teacher':
                    return redirect('teachers/dashboard')
                elif user.user_role=='admin':
                    return redirect('/dashboard')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                newstudent = Student()
                newstudent.user = user  
                newstudent.save()

            elif user.user_role == 'teacher':
                newteacher = Teacher()
                newteacher.user = user
                newteacher.save()



            return redirect('/')

        return render(request, 'users/register.html', {'form': form})

class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'users/profil.html',context={"user":user})


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'users/edit.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profil')
        return render(request, 'users/edit.html', {'form': form})
        
class Create(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/students')

        form = ProfileForm()
        return render(request, 'users/create.html', {'form': form})

class LogautView(View):
    def get(self,request):
        logout(request)
        return redirect("/")

class GroupsView(View):
    def get(self,request):
        teams = Team.objects.all()
        return render(request,'users/groups.html',{"teams":teams})

class StudentView(AdminRequiredMixin, View):
    def get(self, request):
        search_term = request.GET.get('search', '').strip()
        if search_term:
            students = Student.objects.filter(
                Q(user__name__icontains=search_term) | 
                Q(team__name__icontains=search_term)
            )
        else:
            students = Student.objects.all()
        
        return render(request, 'users/student.html', {"students": students})

class StudentByTeam(AdminRequiredMixin,View):
    def get(self,request,id):
        team = get_object_or_404(Team,id=id)
        students = team.students.all()
        return render(request,'users./student.html',{"students":students})


class EditStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit.html', {'form': form})

    def post(self,request,id):
        student = get_object_or_404(Student, id=id)

        form = StudentEditForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students')
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit.html', {'form': form})

class Delete(AdminRequiredMixin,View):
    def get(self,request,id):
        student = get_object_or_404(Student, id=id)
        user = User.objects.get(username=student.user.username)
        student.delete()
        user.delete()
        return redirect('/students')



class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'users/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('/')
        form = ResetPasswordForm()
        return render(request, 'users/reset_password.html', {'form':form})


class AdminDashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/dashboard.html')