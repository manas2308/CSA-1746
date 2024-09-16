planet('Mercury',4879,0.33,57.9).
planet('Venus',12104,4.87,108.2).
planet('Earth',6779,5.97,149.6).
find_planet(Name,Diameter,Mass,Distance):-
    planet(Name,Diameter,Mass,Distance).
