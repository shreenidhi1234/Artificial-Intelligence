% Graph edges with costs
edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 4).
edge(c, d, 1).
edge(d, e, 1).

% Best First Search
best_first_search(Start, Goal, Path, Cost) :-
    best_first([Start], Goal, [Start], Path, 0, Cost).

best_first([Goal|Rest], Goal, _, [Goal|Rest], Cost, Cost).
best_first([Current|Rest], Goal, Visited, Path, CurrentCost, Cost) :-
    findall((Next, C), (edge(Current, Next, C), \+ member(Next, Visited)), Neighbors),
    sort(2, @=<, Neighbors, SortedNeighbors),
    member((Next, C), SortedNeighbors),
    NewCost is CurrentCost + C,
    best_first([Next, Current|Rest], Goal, [Next|Visited], Path, NewCost, Cost).
