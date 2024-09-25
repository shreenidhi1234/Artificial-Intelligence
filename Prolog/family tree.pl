% Family tree facts
parent(john, mary).
parent(john, bob).
parent(susan, mary).
parent(susan, bob).
parent(mary, alice).
parent(mary, david).
parent(bob, james).

% Relationships
father(Father, Child) :- parent(Father, Child), male(Father).
mother(Mother, Child) :- parent(Mother, Child), female(Mother).
grandparent(Grandparent, Grandchild) :- parent(Grandparent, Parent), parent(Parent, Grandchild).
sibling(X, Y) :- parent(Parent, X), parent(Parent, Y), X \= Y.

% Gender facts
male(john).
male(bob).
male(david).
male(james).
female(susan).
female(mary).
female(alice).
