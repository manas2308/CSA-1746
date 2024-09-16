% Facts: fruit(Fruit, Color)
fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(orange, orange).
fruit(lemon, yellow).
fruit(strawberry, red).

% Rule: find_color(Fruit, Color)
find_color(Fruit, Color) :-
    fruit(Fruit, Color).

