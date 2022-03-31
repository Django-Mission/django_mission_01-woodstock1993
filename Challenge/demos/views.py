from django.shortcuts import render
import random

def lotto(request):
    lotto_number = list()

    for _ in range(7):
        number = random.randint(1, 45)
        lotto_number.append(number)

    return render(request, 'lotto.html', {'lotto_number': lotto_number})


def lotto_index(request):
    return render(request, 'lotto_index.html')


def lotto_result(request):
    lotto_number = list()
    game = int(request.GET.get('game'))
    pull_number = [index for index in range(1, 46)]

    for _ in range(game):
        lotto_number.append(random.sample(pull_number, 6))

    return render(request, 'lotto_result.html', {'lotto_number': lotto_number, 'game': game})

