from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User

from game.models import Person,Game,Tile


def index(request):
    top_scores=Person.objects.all().order_by('saved_scores')
    return render(request, 'game/index.html', {'top_scores':top_scores})


def player_score(request):
    top_scores=Person.objects.all().order_by('saved_scores')
    return render(request, 'game/scores.html', {'top_scores':top_scores})

# @login_required
def new_game(request):
    if request.method == 'POST':
        game=Game.objects.create(player=request.user)
        return HttpResponseRedirect(reverse('game:game_play',kwargs={'pk':game.pk}))
    return render(request, 'game/game.html')

def game_play(request,pk):
    game=get_object_or_404(Game,pk=pk)
    return render(request,'game/game_play.html',{'game':game})

def testing_place(request):
    saved_items = Person.objects.all()
    # current_winner = Person.objects.filter(first_name)
    context = {'saved_items': saved_items}
    return render(request, 'game/testing_place.html', context)


def signin(request):
     return render(request, 'game/signin.html', {})

def json_test(request):
    return JsonResponse({'key1':'value1'})

# testing
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def get_tiles(request,pk):
    game=get_object_or_404(Game,pk=pk)
    tiles=[]
    for t in game.tiles.all():
        tiles.append({
            'title':t.title,
            'pk':t.pk,
            'finished':t.finished
        })
    return JsonResponse({"status": "success","tiles":tiles, "points": game.score})

def set_finished(request):
    if request.method == 'POST':
        pk=request.POST.get('pk')

        tile=get_object_or_404(Tile,pk=pk)
        if not tile.game.game_finished:

            tile.finished=True
            tile.save()

            tile.game.score+=10
            tile.game.save()
            if tile.game.score >= 90:
                tile.game.game_finished = True
                tile.game.save()
                request.user.saved_scores += tile.game.score
                request.user.save()
                print("winning score")
            return JsonResponse({"status": "success"})
        else:
            JsonResponse({"status": "game_finished"})
    return JsonResponse({"status": "fail"})
