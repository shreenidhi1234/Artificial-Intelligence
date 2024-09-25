% Initial state: monkey is at door, on the floor, box at window, banana hanging from ceiling
state(at_door, on_floor, at_window, has_not).

% State transitions
move(state(middle, on_box, middle, has_not), grasp, state(middle, on_box, middle, has)).
move(state(P, on_floor, P, H), climb, state(P, on_box, P, H)).
move(state(P1, on_floor, P1, H), push(P1, P2), state(P2, on_floor, P2, H)).
move(state(P1, on_floor, B, H), walk(P1, P2), state(P2, on_floor, B, H)).

% Plan to get the banana
canget(state(_, _, _, has)).
canget(State1) :-
    move(State1, _, State2),
    canget(State2).
