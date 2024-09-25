bird(sparrow).
bird(penguin).
bird(ostrich).

can_fly(sparrow).
cannot_fly(penguin).
cannot_fly(ostrich).

can_fly(Bird) :- bird(Bird), \+ cannot_fly(Bird).

% Query if a bird can fly
can_bird_fly(Bird, 'Yes') :- can_fly(Bird), !.
can_bird_fly(_, 'No').
