# Generated by Django 5.0.7 on 2024-08-21 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payment_link_payment_session_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Последний вход в аккаунт"
            ),
        ),
    ]
