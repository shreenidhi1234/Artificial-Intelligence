% Facts
human(plato).
human(aristotle).

% Rules
mortal(X) :- human(X).

% Backward chaining query
backward_chaining(X) :-
    mortal(X),
    format('~w is mortal.~n', [X]).
