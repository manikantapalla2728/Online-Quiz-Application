CREATE DATABASE quiz_db;
USE quiz_db;

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question VARCHAR(255),
    option1 VARCHAR(100),
    option2 VARCHAR(100),
    option3 VARCHAR(100),
    option4 VARCHAR(100),
    correct_option INT
);

CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    score INT
);

INSERT INTO questions 
(question, option1, option2, option3, option4, correct_option)
VALUES
('What is Python?', 'Snake', 'Programming Language', 'Game', 'OS', 2),
('Which keyword is used to define a function?', 'func', 'define', 'def', 'function', 3),
('Which database is used here?', 'Oracle', 'MongoDB', 'MySQL', 'Firebase', 3);
