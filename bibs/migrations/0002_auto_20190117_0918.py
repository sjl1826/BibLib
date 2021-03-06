# Generated by Django 2.2.dev20180612192205 on 2019-01-17 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Passage',
        ),
        migrations.AddField(
            model_name='book',
            name='chapters',
            field=models.ManyToManyField(to='bibs.Chapter'),
        ),
    ]
