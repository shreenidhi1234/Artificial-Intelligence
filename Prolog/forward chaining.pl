% Facts
human(socrates).

% Rules
mortal(X) :- human(X).

% Forward chaining query
forward_chaining :-
    mortal(X),
    format('~w is mortal.~n', [X]),
    fail.
forward_chaining.
