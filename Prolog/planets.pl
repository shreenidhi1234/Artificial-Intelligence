% Facts about planets
planet(mercury, small, rocky, 0).
planet(venus, small, rocky, 0).
planet(earth, small, rocky, 1).
planet(mars, small, rocky, 2).
planet(jupiter, large, gas_giant, 79).
planet(saturn, large, gas_giant, 83).
planet(uranus, large, ice_giant, 27).
planet(neptune, large, ice_giant, 14).

% Queries
is_rocky(Planet) :-
    planet(Planet, _, rocky, _).

is_gas_giant(Planet) :-
    planet(Planet, _, gas_giant, _).

has_moons(Planet, NumberOfMoons) :-
    planet(Planet, _, _, NumberOfMoons),
    NumberOfMoons > 0.

% Planets with a specific characteristic
planets_with_moons(Moons, Planet) :-
    planet(Planet, _, _, Moons).

planets_of_type(Type, Planet) :-
    planet(Planet, _, Type, _).
