# Generated by Django 5.0.7 on 2024-08-08 15:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата оплаты"),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Сумма оплаты"
                    ),
                ),
                (
                    "payment_type",
                    models.CharField(
                        choices=[
                            ("cash", "Наличные"),
                            ("bank_transfer", "Банковский перевод"),
                        ],
                        max_length=50,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ManyToManyField(
                        blank=True,
                        related_name="payments",
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ManyToManyField(
                        blank=True,
                        related_name="payments",
                        to="materials.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Платеж",
                "verbose_name_plural": "Платежи",
            },
        ),
    ]
