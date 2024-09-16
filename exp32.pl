% Define some facts for pattern matching
person(name(john), 30).
person(name(jane), 25).
person(name(jack), 40).

% Pattern matching rule
match_pattern(Person, Age) :-
    person(name(Person), Age).

