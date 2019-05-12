from django.shortcuts import render


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def welcome(request):
    return render(request, 'welcome.html', {'person': Person('wilfried', 20)})
