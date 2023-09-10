from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Sandria Rania Isanura',
        'class': 'PBP C',
        'npm': '2206025363'
    }

    return render(request, "main.html", context)