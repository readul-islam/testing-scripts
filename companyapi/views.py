from django.http import HttpResponse, JsonResponse
def home_page(request):
    print("Home page requested")
    friends = [
        "akash",
        "batas",
        "sagor"
    ]
    return JsonResponse(friends, safe=False)