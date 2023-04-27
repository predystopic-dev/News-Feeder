from django.shortcuts import render
import csv


def interface(request): return render(request, 'interface/interface.html')


def my_login(request): return render(request, 'interface/my-login.html')


def bias(request): return render(request, 'interface/bias.html')


def display_csv(request):
    with open('D:/Projects/Info/News_Aggregator_Project/interface/data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
        print("Hellop!")
        print(data[0]['title'])
    return render(request, 'interface/interface.html', {'data': data})