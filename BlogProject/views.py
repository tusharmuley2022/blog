from django.http import HttpResponse

def homepage(request):
    # Create an HttpResponse with your desired content
    content = "Welcome to My Homepage\n\nAbout Us: Harsh..."
    
    # Return the HTTP response
    return HttpResponse(content, content_type="text/plain")
