fact(cold).
fact(windy).
rule(stay_inside) :- fact(cold), fact(windy).
rule(take_umbrella) :- fact(rainy).
forward_chaining :-
    (rule(stay_inside) -> assert(fact(stay_inside)); true),
    (rule(take_umbrella) -> assert(fact(take_umbrella)); true),
    list_facts.
list_facts :-
    fact(Fact),
    write(Fact), nl,
    fail.
list_facts.
