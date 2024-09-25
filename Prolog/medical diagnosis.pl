% Symptoms and diseases
disease(flu, [fever, cough, sore_throat]).
disease(cold, [cough, runny_nose, sneezing]).
disease(allergy, [sneezing, runny_nose, itchy_eyes]).

% Diagnosis based on symptoms
diagnosis(Symptoms, Disease) :-
    disease(Disease, DiseaseSymptoms),
    subset(Symptoms, DiseaseSymptoms).
