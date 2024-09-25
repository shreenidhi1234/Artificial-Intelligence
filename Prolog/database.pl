% Database
person('John Doe', '1980-05-15').
person('Jane Smith', '1992-11-23').
person('Emily Davis', '1985-02-10').
person('Michael Brown', '1978-09-12').

% Query to find the DOB of a person
dob(Name, DOB) :-
    person(Name, DOB).
