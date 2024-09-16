diet(diabetes, 'Vegetables', 'Sugary foods').
diet(hypertension, 'Leafy greens', 'Salt').
diet(heart_disease, 'Fatty fish', 'Trans fats').
diet(obesity, 'Whole grains', 'Snacks').
suggest_diet(Disease) :-
    diet(Disease, RecommendedFood, AvoidFood),
    write('For '), write(Disease), write(', you should eat: '), write(RecommendedFood), nl,
    write('And avoid: '), write(AvoidFood), nl.
