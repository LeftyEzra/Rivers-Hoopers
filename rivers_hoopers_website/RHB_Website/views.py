from django.shortcuts import render

# Create your views here.

def home(request):

    #time = datetime.now().strftime("%H:%M")
    #players = Player.objects.all().order_by('jersey_numbers')

    return render(request, 'home.html', {})

