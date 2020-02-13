# Generated by Django 2.2 on 2019-04-13 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_year', models.DateTimeField(verbose_name='date published')),
                ('document_abstract', models.CharField(max_length=1000)),
                ('document_journal', models.CharField(max_length=50)),
                ('document_authors', models.CharField(max_length=50)),
            ],
        ),
    ]