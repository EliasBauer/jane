from django.shortcuts import render

# views = Endpoint


def main(request):
    return render(request, "egal")
