# Generated by Django 5.0.4 on 2024-04-20 17:29

import django.db.models.deletion
import task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='task.district')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhoods', to='task.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_appartment', models.IntegerField()),
                ('ownership', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('category_appartment', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='task.district')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='task.neighborhood')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='task.region')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('residential_status', models.CharField(max_length=255)),
                ('passport_number', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('age', models.CharField(blank=True, max_length=50, null=True)),
                ('jshshir', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=255)),
                ('appartment_type', models.CharField(max_length=255)),
                ('cadastr_number', models.CharField(max_length=255)),
                ('status_of_registration', models.CharField(max_length=255)),
                ('time_registered', models.DateField()),
                ('address_of_passport', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=task.models.upload_to)),
                ('gender', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='task.district')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='task.house')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='task.neighborhood')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='task.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='district',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='task.region'),
        ),
        migrations.CreateModel(
            name='Relative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('document_type', models.CharField(max_length=255)),
                ('document_series', models.CharField(max_length=20)),
                ('document_number', models.IntegerField()),
                ('kinship', models.CharField(max_length=255)),
                ('jshshir', models.BigIntegerField()),
                ('phone_number', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('disability', models.CharField(max_length=255)),
                ('war_participant', models.BooleanField(default=False)),
                ('no_breadwinner', models.BooleanField(default=False)),
                ('lonely_old_man', models.BooleanField(default=False)),
                ('difficult_condition', models.BooleanField(default=False)),
                ('behind_war', models.BooleanField(default=False)),
                ('gone_for_along_time', models.BooleanField(default=False)),
                ('participant_of_AES', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relatives', to='task.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='task.district')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='task.neighborhood')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='task.region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='task.street'),
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='task.street'),
        ),
    ]
