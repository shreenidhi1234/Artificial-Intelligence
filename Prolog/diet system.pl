% Disease and dietary recommendations
diet(diabetes, 'Low sugar diet').
diet(hypertension, 'Low salt diet').
diet(obesity, 'Low fat diet').
diet(anemia, 'Iron-rich diet').

% Query for diet based on disease
diet_recommendation(Disease, Diet) :- diet(Disease, Diet).
