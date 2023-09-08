from django.db import models
from datetime import timedelta
from django.contrib.auth.models import User
import stripe
import os
from django.core.exceptions import ValidationError
from djstripe.models import Product




class CourseCategory(models.Model):
    name = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='categoryimgs', blank=True, null=True, verbose_name="Category Image", default='categoryimgs/original-9cc30d293a2efd79103e7add6d16b0be.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Course Categories'
    
class Language(models.Model):
    language = models.CharField(null=True, max_length=256)
    def __str__(self):
        return self.language

stripe.api_key = os.environ.get('STRIPE_TEST_SECRET_KEY')

class Course(models.Model):
    title = models.CharField(max_length=200)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(CourseCategory, related_name='courses', blank=True)
    description = models.TextField(blank=True)  # Changed to TextField for longer descriptions
    course_image = models.ImageField(upload_to='courseimgs', blank=True, null=True, verbose_name="Course Image", default='courseimgs/70-702065_django-python-logo-apress-the-definitive-guide-to_T18MEpY.png')
    certificate = models.ImageField(upload_to='certimgs', blank=True, null=True, verbose_name="Certificate Image", default='certimgs/Navy_and_Gold_Geometric_Luxury_Modern_Certificate.png')
    duration = models.DurationField(default=timedelta(weeks=12))
    activation_status = models.BooleanField(default=False)
    registered_users = models.ManyToManyField(User, related_name='registered_courses', blank=True)
    recurring_payment = models.BooleanField(default=False)
    onetime_payment = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    has_discount = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    languages = models.ManyToManyField(Language, related_name="related_languages", blank=True)
    strip_id = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):

        product = Product.objects.filter(name=self.title).first()
        if product:
            raise ValidationError('Course Already exists!!')

        if not product:
            # Create the product on Stripe
            stripe_product = stripe.Product.create(
                name=self.title,
                type='service',  # Adjust the type as needed
            )
        self.strip_id = stripe_product['id']
        # Save the Course instance
        super().save(*args, **kwargs)


    @property
    def users_count(self):
        return self.registered_users.count()
    
    class Meta:
        verbose_name_plural = 'Courses'




class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    course_module_image = models.ImageField(upload_to='courseimgs', blank=True, null=True, verbose_name="Course Module Image", default='courseimgs/70-702065_django-python-logo-apress-the-definitive-guide-to_T18MEpY.png')
    activation_status = models.BooleanField(default=False)
    course_video = models.FileField(upload_to='coursevids', default='coursevids/original-cc0696de49d294a0c72f89b52e5cf52a.mp4')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Modules'
   



class CourseSubModule(models.Model):
    course_module = models.ForeignKey(CourseModule, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    course_video = models.FileField(upload_to='coursevids', default='coursevids/original-cc0696de49d294a0c72f89b52e5cf52a.mp4')
    course_image = models.ImageField(upload_to='courseimgs', blank=True, null=True, verbose_name="Course SubModule Image", default='courseimgs/70-702065_django-python-logo-apress-the-definitive-guide-to_T18MEpY.png')
    activation_status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Sub Modules'
    

class CourseSubModuleQuiz(models.Model):
    course_sub_module = models.ForeignKey(CourseSubModule, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Sub Module Quizzes'
        

class CourseModuleQuiz(models.Model):
    course_module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField(default='_')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Module Quizzes'
    

class CourseModuleQuizAnswer(models.Model):
    module_question = models.ForeignKey(CourseModuleQuiz, on_delete=models.CASCADE)
    answers = models.TextField()
    correct_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Module Quiz Answers'

    def __str__(self):
        return f"Answers for: {self.module_question.question}"

class CourseSubModuleQuizAnswer(models.Model):
    sub_module_question = models.ForeignKey(CourseSubModuleQuiz, on_delete=models.CASCADE)
    answers = models.TextField()
    correct_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Sub Module Quiz Answers'
        

    def __str__(self):
        return self.answers

class CourseReview(models.Model):
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    reviewmsg = models.TextField(default='A very nice course')

    def __str__(self):
        return self.reviewmsg

    class Meta:
        verbose_name_plural = 'Course Reviews'
      


