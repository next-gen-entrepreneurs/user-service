from django.http import HttpResponse

def health_check(request):
    """
    A simple view to return a 200 OK for health checks.
    """
    return HttpResponse("OK", status=200)
