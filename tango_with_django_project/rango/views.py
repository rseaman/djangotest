from django.http      import HttpResponse
from django.template  import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Get context of request
    context = RequestContext(request)

    # Dictionary to be passed to template engine
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return rendered response
    return render_to_response('rango/index.html', context_dict, context)


def about(request):
    return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Index</a>")