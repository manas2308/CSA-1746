bird(sparrow,yes).
bird(eagle,yes).
bird(pheonix,yes).
bird(penguin,no).
bird(ostrich,no).
bird(parrot,yes).
bird(kiwi,no).
fly(Bird):-
    bird(Bird, yes),
    write(Bird), write('can fly'), nl.
fly(Bird):-
    bird(Bird, no),
    write(Bird), write('cannot fly'), nl.

