% Facts
fact(cold).
fact(windy).
fact(rainy).

% Rules
rule(stay_inside) :- fact(cold), fact(windy).
rule(take_umbrella) :- fact(rainy).

% Backward chaining
backward_chaining(Goal) :-
    (rule(Goal) -> write(Goal), nl;
    (Goal = stay_inside ->
        (fact(cold), fact(windy) -> write(stay_inside), nl; true);
    Goal = take_umbrella ->
        (fact(rainy) -> write(take_umbrella), nl; true))).

