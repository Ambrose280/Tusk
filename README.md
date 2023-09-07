API Documentation

# To get the detail of any Data Set, Use the ID 
# Example Data:
# {
        "id": 12,
        "title": "Web Development",
        "description": "Learn how to build things for the web",
        "course_image": "/media/courseimgs/70-702065_django-python-logo-apress-the-definitive-guide-to_T18MEpY.png",
        "certificate": "/media/certimgs/Navy_and_Gold_Geometric_Luxury_Modern_Certificate.png",
        "duration": "84 00:00:00",
        "activation_status": true,
        "recurring_payment": true,
        "onetime_payment": false,
        "price": "50000.00",
        "has_discount": true,
        "discount_percentage": "20.00",
        "vendor": 2,
        "category": [
            1,
            2
        ],
        "registered_users": [
            1,
            2,
            3
        ]
    }
# To get the detail you api/v1/coursedetail/12 to get the Above Data. The same Implies to other endpoints
# The 1st endpoint e.g http://127.0.0.1:8000/api/v1/courses/ supports GET and POST requests. 
# The detail supports only GET, PUT and DELETE
# To know the HTTP Verbs supported by an endpoint, visit the swagger documentation or API Home Page

api/v1/courses/
api/v1/courses/?query=coursetitle
api/v1/coursedetail/<int:pk>

api/v1/coursecategories/
api/v1/coursecategory/<int:pk>
api/v1/coursecategories/?query=categoryname

api/v1/coursemodules/
api/v1/coursemodule/<int:pk>

api/v1/coursesubmodules/
api/v1/coursesubmodule/<int:pk>

api/v1/coursemodulequizzes/
api/v1/coursemodulequiz/<int:pk>

api/v1/coursesubmodulequizzes/
api/v1/coursesubmodulequiz/<int:pk>

api/v1/coursemodulequizanswers/
api/v1/coursemodulequizanswer/<int:pk>

api/v1/coursesubmodulequizanswers/
api/v1/coursesubmodulequizanswer/<int:pk>

api/v1/coursereviews/
api/v1/coursereview/<int:pk>

api/v1/coursepaymentlogs/
api/v1/coursepayment/<int:pk>


