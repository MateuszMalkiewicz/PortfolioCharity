def app_context(request):
    ctx = {
           'user': request.user
           }
    return ctx
