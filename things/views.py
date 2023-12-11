from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse

def home_view(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Things</title>
    </head>
    <body>
        <h1>Things</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
