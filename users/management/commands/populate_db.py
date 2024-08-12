from django.contrib.auth.models import Group
from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.create_groups()
        self.create_users()
        self.create_courses()
        self.create_lessons()
        self.create_payments()
        self.stdout.write(self.style.SUCCESS("База данных успешно заполнена!"))

    def create_groups(self):
        self.croup1 = Group.objects.get_or_create(name="moders")

    def create_users(self):
        self.user1 = User.objects.create(email="user1@gmail.com", password="password1")
        self.user1.groups.add(Group.objects.get(name="moders"))

        self.user2 = User.objects.create(email="user2@gmail.com", password="password2")

    def create_courses(self):
        self.course1 = Course.objects.create(
            name="Django", description="Старый добрый Django"
        )
        self.course2 = Course.objects.create(
            name="DRF", description="Django REST framework"
        )

    def create_lessons(self):
        self.lesson1 = Lesson.objects.create(
            name="Знакомство с Django",
            description="Основы Django",
            video_link="https://example.com/lesson1",
            course=self.course1,
        )
        self.lesson2 = Lesson.objects.create(
            name="Сериализаторы",
            description="REST API",
            video_link="https://example.com/lesson2",
            course=self.course2,
        )

    def create_payments(self):
        self.payment1 = Payment.objects.create(
            user=self.user1,
            amount=20000.00,
            payment_type="bank_transfer",
        )
        self.payment1.paid_course.set([self.course1])
        self.payment1.paid_lesson.set([self.lesson1])

        self.payment2 = Payment.objects.create(
            user=self.user2,
            amount=30000.00,
            payment_type="cash",
        )
        self.payment2.paid_course.set([self.course2])
