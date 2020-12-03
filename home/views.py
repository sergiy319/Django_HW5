from django.shortcuts import render


# Create the required function.
def show_string(request):
    return render(request, 'index.html', context={'name': 'World!'})
