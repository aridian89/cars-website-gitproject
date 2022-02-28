# Generated by Django 4.0.2 on 2022-02-25 20:10

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_registeration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('ABS', 'ABS'), ('AM/FM Radio', 'AM/FM Radio'), ('Air Bags', 'Air Bags'), ('Air Conditioning', 'Air Conditioning'), ('Alloy Rims', 'Alloy Rims'), ('Cool Box', 'Cool Box'), ('Cruise Control', 'Cruise Control'), ('DVD Player', 'DVD Player'), ('Sunroof', 'Sunroof'), ('Power Steering', 'Power Steering')], max_length=500),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]