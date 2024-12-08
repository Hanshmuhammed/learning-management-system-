from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Add related_name to avoid clashes with the default auth.User model
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Customize the related_name to avoid conflict
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Customize the related_name to avoid conflict
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Course(models.Model):
    CATEGORY_CHOICES = [
        ('web_design', 'Web Design'),
        ('graphic_design', 'Graphic Design'),
        ('video_editing', 'Video Editing'),
        ('online_marketing', 'Online Marketing'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use settings.AUTH_USER_MODEL instead of direct User reference
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}
    )

    def __str__(self):
        return self.title


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.course.title}"


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use settings.AUTH_USER_MODEL for User
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    submission_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='assignments/')

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"


class InstructorProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # Use settings.AUTH_USER_MODEL
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},  # Only allow users with the 'teacher' role
    )
    photo = models.ImageField(upload_to='instructors/', blank=True, null=True)
    qualifications = models.TextField()

    def __str__(self):
        return self.user.username


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"










