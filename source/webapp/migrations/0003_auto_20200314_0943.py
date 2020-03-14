# Generated by Django 2.2 on 2020-03-14 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_auto_20200314_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='author',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_file', to='webapp.File')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='private_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Приват',
                'verbose_name_plural': 'Приват',
            },
        ),
    ]