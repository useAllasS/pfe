# Generated by Django 3.0.5 on 2023-04-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/profile_pic/CustomerProfilePic/defualt.png', null=True, upload_to='profile_pic/CustomerProfilePic/'),
        ),
    ]
