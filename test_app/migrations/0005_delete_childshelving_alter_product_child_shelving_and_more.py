# Generated by Django 4.2.6 on 2023-10-15 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_childshelving_remove_shelving_additional_shelving_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildShelving',
        ),
        migrations.AlterField(
            model_name='product',
            name='child_shelving',
            field=models.ManyToManyField(blank=True, related_name='child_shelving', to='test_app.shelving'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shelving',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shelving', to='test_app.shelving'),
        ),
    ]
