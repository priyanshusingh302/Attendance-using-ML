from recognition import views
from users import views
from django import template

register = template.Library()


def is_Employee(user):
    return not user.groups.filter(name='Employee').exists()

