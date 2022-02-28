from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):
    make_choices = (
    ('Suzuki','Suzuki'),
    ('Toyota','Toyota'),
    ('Honda','Honda'),
    ('Kia','Kia'),
    ('Dahaitsu','Dahaitsu'),
    )
    cities_choices = (
    ('ISB','Islamabad'),
    ('RWP','Rawalpindi'),
    ('GJR','Gujranwala'),
    ('KHI','Karachi'),
    ('FSD','Faisalabad'),
    ('LHE','Lahore'),
    )
    year_choice = []
    for r in range(1920,(datetime.now().year+1)):
        year_choice.append((r,r))
    feature_choices = (
        ('ABS','ABS'),
        ('AM/FM Radio','AM/FM Radio'),
        ('Air Bags','Air Bags'),
        ('Air Conditioning','Air Conditioning'),
        ('Alloy Rims','Alloy Rims'),
        ('Cool Box','Cool Box'),
        ('Cruise Control','Cruise Control'),
        ('DVD Player','DVD Player'),
        ('Sunroof','Sunroof'),
        ('Power Steering','Power Steering'),

    )

    cities = models.CharField(choices=cities_choices,max_length=100)
    registeration = models.CharField(choices=cities_choices,max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    assemble = models.CharField(max_length=100)
    engine_capacity = models.IntegerField()
    body_type = models.CharField(max_length=100)
    make = models.CharField(choices=make_choices,default='Honda',max_length=200)
    features = MultiSelectField(choices=feature_choices,max_length=500)
    no_of_owner = models.IntegerField()
    price = models.IntegerField()
    description = RichTextField()
    transmition = models.CharField(max_length=100)
    milage = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    fuel_type = models.CharField(max_length=100)
    feature_image = models.ImageField(upload_to='photo/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/',blank=True)
    car_photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/',blank=True)
    car_photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/',blank=True)
    car_photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/',blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.model
