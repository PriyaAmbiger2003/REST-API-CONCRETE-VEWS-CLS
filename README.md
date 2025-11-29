🧩 Django REST API – Concrete & Generic Views (Advanced Project)

This project demonstrates an advanced Django REST Framework (DRF) setup using:

Generic Views

Concrete Views

Inheritance-based custom view classes

Serializers

Models

Organized URL structure

A complete RESTful CRUD API for Product

This project is ideal for understanding how to combine ListAPIView + CreateAPIView, Retrieve + Update + Destroy, and other DRF features in a real-world project structure.

🚀 Features
🔹 Product API (Full CRUD)

Includes:

Method	Endpoint	Description
GET	/products/	List all products
POST	/products/	Create a new product
GET	/products/<id>/	Retrieve a single product
PUT / PATCH	/products/<id>/	Update product
DELETE	/products/<id>/	Delete product
🔹 Uses Advanced DRF Class-Based Views

ListAPIView + CreateAPIView (merged using inheritance)

RetrieveAPIView + UpdateAPIView + DestroyAPIView (combined)

ListCreateAPIView

RetrieveUpdateDestroyAPIView

🔹 Clean and Scalable Project Structure

Everything organized in a Django app with:

models.py

serializers.py

views.py

urls.py

And global URL configuration in project directory.

📂 Project Structure
project/
│── project/
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│   └── asgi.py
│
│── app/
│   │── models.py
│   │── serializers.py
│   │── views.py
│   │── urls.py
│   └── apps.py
│
│── manage.py
└── requirements.txt

🛠️ Tech Stack

Python 3.x

Django

Django REST Framework (DRF)

SQLite (default)

🧱 Models (example)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()

🔄 Serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

🧠 Views (Advanced – Inheritance Based)
List + Create Product
class ListCreateProductView(ListAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

Retrieve + Update + Delete Product
class RetrieveUpdateDestroyProductView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

🌐 API URLs

app/urls.py

from django.urls import path
from .views import ListCreateProductView, RetrieveUpdateDestroyProductView

urlpatterns = [
    path('products/', ListCreateProductView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', RetrieveUpdateDestroyProductView.as_view(), name='product-detail'),
]


project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/YourUsername/REST-API-CONCRETE-VIEWS-CLS.git
cd REST-API-CONCRETE-VIEWS-CLS

2️⃣ Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt:

pip install django djangorestframework

3️⃣ Run migrations
python manage.py migrate

4️⃣ Start the server
python manage.py runserver

5️⃣ Test API in browser / Postman

http://127.0.0.1:8000/products/

http://127.0.0.1:8000/products/1/

📌 Future Enhancements

Add authentication (Token / JWT)

Add pagination

Add filtering & search

Add permissions (Admin only for delete/update)

Add Swagger API Documentation

🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to improve.

📄 License

This project is open-source under the MIT License.

If you want, I can also create your:

✅ requirements.txt
✅ .gitignore for Django
✅ API documentation (Postman-style)
Just tell me!
