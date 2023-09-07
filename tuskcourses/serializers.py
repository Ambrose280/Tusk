from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from djstripe.models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceItemSerializer(ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

class SubscriptionItemSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionItem
        fields = '__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PaymentIntentSerializer(ModelSerializer):
    class Meta:
        model = PaymentIntent
        fields = '__all__'

class PayoutSerializer(ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'

class SetupIntentSerializer(ModelSerializer):
    class Meta:
        model = SetupIntent
        fields = '__all__'

class RefundSerializer(ModelSerializer):
    class Meta:
        model = Refund
        fields = '__all__'

class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class SubscriptionScheduleSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionSchedule
        fields = '__all__'

class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'



class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'

        
class CourseCategorySerializer(ModelSerializer):

    class Meta:
        model = CourseCategory
        fields = '__all__'
        # ('id', 'name')

class CourseUsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # ('id', 'username')

class CourseSerializer(ModelSerializer):
    # registered_users = CourseUsersSerializer(many=True, read_only=True)
    # category = CourseCategorySerializer(many=True, read_only=True)
    # vendor = serializers.ReadOnlyField(source='vendor.username')
    
    class Meta:
        model = Course
        fields = '__all__'
        # (
        #     'id', 'title', 'vendor', 'category', 'description', 
        #     'course_image', 'certificate', 'duration', 'activation_status',
        #     'registered_users',  # Include the new fields
        # )

    

class CourseModuleSerializer(ModelSerializer):
    # course_name = serializers.ReadOnlyField(source='course.title')
  
    class Meta:
        model = CourseModule
        
        fields = '__all__'
        # (
        #     'id', 'course_name', 'title', 'course_module_image', 'activation_status', 
        #     'course_video',   # Include the new fields
        # )



class CourseSubModuleSerializer(ModelSerializer):
    # course_module = serializers.ReadOnlyField(source='course_module.title')
    class Meta:
        model = CourseSubModule
        fields = '__all__'
        # ('id', 'title', 'description', 'course_video', 'course_image', 'activation_status', 'course_module')



class CourseSubModuleQuizSerializer(ModelSerializer):
    # course_sub_module = serializers.ReadOnlyField(source='course_sub_module.title')
    class Meta:
        model = CourseSubModuleQuiz
        fields = '__all__'
        # ('id', 'course_sub_module', 'question')

class CourseModuleQuizSerializer(ModelSerializer):
    # course_module = serializers.ReadOnlyField(source='course_module.title')
    class Meta:
        model = CourseModuleQuiz
        fields = '__all__'
        # ('id', 'course_module', 'question')

class CourseModuleQuizAnswerSerializer(ModelSerializer):
    # module_question = serializers.ReadOnlyField(source='module_question.question')
    class Meta:
        model = CourseModuleQuizAnswer
        fields = '__all__'
        # ('id', 'module_question', 'answers', 'correct_status',)

class CourseSubModuleQuizAnswerSerializer(ModelSerializer):
    # sub_module_question = serializers.ReadOnlyField(source='sub_module_question.question')

    class Meta:
        model = CourseSubModuleQuizAnswer
        fields = '__all__'
        # ('id', 'sub_module_question', 'answers', 'correct_status',)

class CourseReviewSerializer(ModelSerializer):
    course = serializers.ReadOnlyField(source='course.title')
    # reviewed_by = serializers.ReadOnlyField(source='reviewed_by.username')
    
    class Meta:
        model = CourseReview
        fields = '__all__'
        # ('id', 'reviewed_by', 'rating', 'date', 'course', 'reviewmsg',)




