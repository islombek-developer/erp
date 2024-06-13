from django.db import models
from users.models import Team,Student

class Lesson(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=100, unique=True)
    date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    homework_status = models.BooleanField(default=False)


    class Meta:
        unique_together = ['team', 'title']

    def __str__(self):
        return self.title


class Homework(models.Model):
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name='homework')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='homeworks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    description = models.TextField()
    homework_file = models.FileField(upload_to='homeworks', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['student', 'team']

    def __str__(self):
        return f"{self.student.user.first_name}-- {self.lesson.title}"
