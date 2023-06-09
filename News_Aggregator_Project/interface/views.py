from django.shortcuts import render
import csv


def interface(request): return render(request, 'interface/interface.html')


def bias(request): return render(request, 'interface/bias.html')


def display_csv(request):
    with open('interface/data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return render(request, 'interface/interface.html', {'data': data})