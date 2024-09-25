% Facts
student(john, math101).
student(mary, math101).
student(john, sci102).
student(mary, eng103).
student(paul, sci102).
student(paul, eng103).

teacher(mr_smith, math101).
teacher(ms_jones, sci102).
teacher(mrs_brown, eng103).

% Rules
teaches(Teacher, Student, SubjectCode) :-
    student(Student, SubjectCode),
    teacher(Teacher, SubjectCode).

% Queries
teacher_of(Student, Teacher) :-
    student(Student, SubjectCode),
    teacher(Teacher, SubjectCode).

subject_of(Student, SubjectCode) :-
    student(Student, SubjectCode).
