from django.shortcuts import render


def handle_not_found(request, exception):
    return render(request, 'core/not-found.html')


def handle_server_error(request):
    return render(request, 'core/server-error.html')