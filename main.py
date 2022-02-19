import request


for i in range(40):
    print(request.get_summoner('insane meow'))
print(f'called {i+1} times')