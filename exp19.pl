person('Manas',date(2005,2,23)).
person('Kishan',date(1995,12,25)).
person('Sunny',date(1990,3,15)).
find_person(Name, date(Year,Month,Day)):-
    person(Name, date(Year,Month,Day)).

