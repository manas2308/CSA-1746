edge(a, b).
edge(a, c).
edge(b, d).
edge(b, e).
edge(c, f).
edge(d, g).
edge(e, h).
edge(f, i).
bfs(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).
bfs([[Goal | Path] | _], Goal, [Goal | Path]).
bfs([Path | Paths], Goal, Solution) :-
    extend(Path, NewPaths),
    append(Paths, NewPaths, UpdatedPaths),
    bfs(UpdatedPaths, Goal, Solution).
extend([Node | Path], NewPaths) :-
    findall([NextNode, Node | Path],
            (edge(Node, NextNode), \+ member(NextNode, [Node | Path])),
            NewPaths).

