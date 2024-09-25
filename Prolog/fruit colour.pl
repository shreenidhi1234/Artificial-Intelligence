fruit(apple, red).
fruit(banana, yellow).
fruit(grape, purple).
fruit(lemon, yellow).
fruit(orange, orange).

% Query for fruit color
fruit_color(Fruit, Color) :- fruit(Fruit, Color).
