% Base case: the sum of the first 1 odd number is 1
sum_odd(1, 1).

% Recursive case: the sum of the first N odd numbers
sum_odd(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_odd(N1, Sum1),
    OddNumber is 2 * N - 1,
    Sum is Sum1 + OddNumber.
