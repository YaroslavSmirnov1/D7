# Generated by Django 4.0.1 on 2022-02-02 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.base
import django.views.generic.edit


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryView',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newapp.category')),
            ],
            bases=(django.views.generic.edit.FormView, django.views.generic.base.View, 'newapp.category'),
        ),
        migrations.CreateModel(
            name='CategoryView2',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='newapp.category')),
            ],
            bases=(django.views.generic.edit.FormView, django.views.generic.base.View, 'newapp.category'),
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]