disease(fever, flu).
disease(cough, flu).
disease(fatigue, flu).
disease(headache, flu).
disease(runny_nose, cold).
disease(sneezing, cold).
disease(sore_throat, cold).
disease(body_ache, flu).
disease(itchy_eyes, allergy).
disease(skin_rash, allergy).
disease(sneezing, allergy).
disease(cough, allergy).
diagnose(Disease, Symptoms) :-
    all_symptoms_match(Disease, Symptoms).
all_symptoms_match(Disease, Symptoms) :-
    maplist(symptom_for_disease(Disease), Symptoms).
symptom_for_disease(Disease, Symptom) :-
    disease(Symptom, Disease).
