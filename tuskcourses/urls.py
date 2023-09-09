from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('stripeproducts/', views.stripe_products, name= "setupintents"),
    path('stripeproduct/<int:pk>', views.stripe_product_detail, name='setupintent'),


    path('stripesetupintents/', views.setupintent, name= "setupintents"),
    path('stripesetupintent/<int:pk>', views.setupintent_detail, name='setupintent'),

    path('stripepaymentintents/', views.payment_intents, name= "setupintents"),
    path('stripepaymentintent/<int:pk>', views.payment_intent, name='setupintent'),

    path('striperefunditems/', views.refunditems, name= "refunditems"),
    path('striperefunditem/<int:pk>', views.refunditem, name='refunditem'),

    path('paymentmethods/', views.paymentmethods, name= "refunditems"),
    path('paymentmethod/<int:pk>', views.paymentmethod, name='refunditem'),

    path('stripesubscriptions/', views.subscriptionitems, name= "subscriptionitems"),
    path('stripesubscription/<int:pk>', views.subscriptionitem, name='subscriptionitem'),

    path('stripesessions/', views.sessionlist, name= "sessions"),
    path('stripesessiondetail/<int:pk>', views.session_detail, name='sessiondetail'),

    path('stripeplans/', views.plan, name= "plans"),
    path('stripeplandetail/<int:pk>', views.plan_detail, name='plandetail'),

    path('stripeprices/', views.stripe_prices, name= "stripeprices"),
    path('stripeprice/<int:pk>', views.stripe_price_detail, name='stripeprice'),


    path('users/', views.users, name= "users_list"),
    path('user/<int:pk>', views.user_detail, name='user_detail'),

    path('languages/', views.languages, name= "users_list"),
    path('language/<int:pk>', views.language_detail, name='user_detail'),

    path('courses/', views.courses_list, name= "courses_list"),
    path('coursedetail/<int:pk>', views.course_details, name='course_detail'),
    
  
    path('coursecategories/', views.course_categories_list, name='course_categories'),
    path('coursecategory/<int:pk>', views.course_categories_details, name='course_category'),
    

    path('coursemodules/', views.course_modules_list, name='course_modules'),
    path('coursemodule/<int:pk>', views.course_module_details, name='course_module'),

  
    path('coursesubmodules/', views.course_sub_modules_list, name='course_sub_module'),
    path('coursesubmodule/<int:pk>', views.course_sub_module_details, name='course_sub_module_detail'),

  
    path('coursemodulequizzes/', views.course_module_quizzes, name='course_module_quizzes'),
    path('coursemodulequiz/<int:pk>', views.course_module_quizzes_details, name='course_module_quiz_detail'),

    
    path('coursesubmodulequizzes/', views.course_sub_module_quizzes, name='course_sub_module_quizzes'),
    path('coursesubmodulequiz/<int:pk>', views.course_sub_module_quizzes_details, name='course_sub_module_quiz'),

   
    path('coursemodulequizanswers/', views.course_module_quiz_answers, name='course_module_quiz_answers'),
    path('coursemodulequizanswer/<int:pk>', views.course_module_quiz_answers_details, name='course_module_quiz_answer'),

  
    path('coursesubmodulequizanswers/', views.course_sub_module_quiz_answers, name='course_sub_module_quiz_answers'),
    path('coursesubmodulequizanswer/<int:pk>', views.course_sub_module_quiz_answers_details, name='course_sub_module_quiz_answer'),

    
    path('coursereviews/', views.course_reviews, name='course_reviews'),
    path('coursereview/<int:pk>', views.course_review_details, name='course_reviews'),
]


