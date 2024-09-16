% Define the vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

% Count vowels in a string
count_vowels(String, Count) :-
    string_chars(String, Chars),
    count_vowels_list(Chars, 0, Count).

% Helper predicate to count vowels in a list of characters
count_vowels_list([], Count, Count).
count_vowels_list([Char | Rest], Acc, Count) :-
    (   vowel(Char)
    ->  NewAcc is Acc + 1
    ;   NewAcc is Acc
    ),
    count_vowels_list(Rest, NewAcc, Count).

% Example query:
% ?- count_vowels("hello world", Count).
