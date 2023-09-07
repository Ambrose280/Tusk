from django.contrib import admin
from .models import *
from django.contrib.admin.sites import AdminSite

from django.contrib.admin.sites import AdminSite

from .models import *

import admin_thumbnails


AdminSite.site_header = "WebTusk Administration"
AdminSite.site_title = "WebTusk Administration"

AdminSite.index_title = "Authorized Personnel Only"


@admin_thumbnails.thumbnail('course_image')
@admin_thumbnails.thumbnail('certificate')
class CourseAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'title', 'vendor', 'duration', 'certificate_thumbnail', 'activation_status', 'course_image_thumbnail', 'users_count', 'calculate_discounted_price')
    list_filter = ('title',)
    search_fields = ('title',)

     # Custom column header
@admin_thumbnails.thumbnail('course_module_image')
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'activation_status', 'course_video','course_module_image_thumbnail')
    list_filter = ('title',)
    search_fields = ('title',)

@admin_thumbnails.thumbnail('course_image')
class CourseSubModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course_module', 'course_video', 'activation_status','course_image_thumbnail')
    list_filter = ('description', 'title')
    search_fields = ('description', 'title')



class Course_UserAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin_thumbnails.thumbnail('category_image')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_image_thumbnail')
    list_filter = ('name',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'reviewed_by', 'date', 'rating', 'reviewmsg')
    list_filter = ('reviewed_by',)
    search_fields = ('reviewed_by',)

class CourseModuleQuizAnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_question', 'answers', 'correct_status')
    list_filter = ('module_question', 'answers')
    search_fields = ('reviewed_by', 'answers')

class CourseSubModuleQuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'course_sub_module',)
    list_filter = ('question', 'course_sub_module')
    search_fields = ('question', 'course_sub_module')

class CourseModuleQuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'course_module',)
    list_filter = ('question', 'course_module')
    search_fields = ('question', 'course_module')

class CourseSubModuleQuizAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answers', 'sub_module_question', 'correct_status')
    list_filter = ('sub_module_question', 'answers')
    search_fields = ('sub_module_question', 'answers')



class CourseUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'courses_count', 'subscription_status')
    list_filter = ('user', 'courses')
    search_fields = ('user', 'courses')



admin.site.register(CourseSubModuleQuizAnswer, CourseSubModuleQuizAnswerAdmin)
admin.site.register(CourseModuleQuiz, CourseModuleQuizAdmin)
admin.site.register(CourseSubModuleQuiz, CourseSubModuleQuizAdmin)
admin.site.register(CourseModuleQuizAnswer, CourseModuleQuizAnswersAdmin)
admin.site.register(CourseSubModule, CourseSubModuleAdmin)
admin.site.register(CourseReview, ReviewAdmin)
admin.site.register(Course, CourseAdmin)

admin.site.register(CourseModule, CourseModuleAdmin)
admin.site.register(CourseCategory, CategoryAdmin)
admin.site.register(Language)