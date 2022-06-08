"""Restaurant rating lister."""


# put your code here
from audioop import add


all_resturants = { 'Florean Fortescues Ice Cream Parlour' :4,
'Jellied Eel Shop' :3,
'The Tavern' :3,
'Luchino Caffe' :1,
'The Porcupine' :5,
'Diagon Alley cafe' :2,
'The Bear & Staff' :2,
'Ministry Munchies' :1,
'Chip Shop' :3,
"Eternelle's Elixir of Refreshment" :5,
'Big Bean Shack' :3,
'The Club' :2
}

def get_resturants():
    sorted_resturants = sorted(all_resturants.items())
    for key, value in sorted_resturants:
        print(key, ':', value)
        
    print('Here are all the resturants with ratings')

get_resturants()

resturant = input('Which resturant would you like to add?\n')
resturant_rating = input('Enter your rating.\n')

all_resturants[resturant] = resturant_rating

for key, value in all_resturants.items():
    print(key, ':', value)


    