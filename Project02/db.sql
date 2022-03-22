
CREATE TABLE IF NOT EXISTS Students(
    StudentID Varchar(6) PRIMARY KEY,
    FullName Varchar(30) NOT NULL,
    Birthday DATETIME NOT NULL,
    Sex TINYINT NOT NULL,
    Place Varchar(500),
    Phone Varchar(11) NOT NULL,
    Email Varchar(100) NOT NULL
)

CREATE TABLE IF NOT EXISTS Subjects(
    SubjectID Varchar(6) PRIMARY KEY,
    SubName Varchar(20) NOT NULL
)

CREATE TABLE IF NOT EXISTS Scores(
    StudentID Varchar(6) FOREIGN KEY REFERENCES Students(studentID),
    SubjectID Varchar(6) FOREIGN KEY REFERENCES Subjects(SubjectID),
    Score1 int NOT NULL,
    Score2 int NOT NULL,
    PRIMARY KEY (StudentID, SubjectID)
)

INSERT INTO Students(StudentID, FullName, Birthday, Sex, Place, Phone, Email)
VALUES
    ("ST0001", "Cuong Nguyen", "17/08/1994", 1, "Việt Nam", "0977677010", "cuongnhict@gmail.com"),
    ("ST0002", "Tường An", "17/08/1994", 0, "Nhật Bản", "0977677010", "tuongan@gmail.com"),
    ("ST0003", "Như Phương", "17/08/1994", 0, "Nhật Bản", "0977677010", "nhuphuong@gmail.com"),
    ("ST0004", "Phương Thảo", "02/02/2002", 0, "Việt Nam", "0977777777", "phuongthao@gmail.com"),
    ("ST0005", "Trọng Nghĩa", "01/01/2000", 1, "Nhật Bản", "1111111111", "nghia@gmail.com"),
    ("ST0006", "Đồng Tài", "03/03/2003", 1, "Nhật Bản", "1111111111", "tai@gmail.com");

INSERT INTO Subjects(SubjectID, SubName)
VALUES
	("SU0001", "Database"),
	("SU0002", "Basic Python"),
	("SU0003", "Advanced Python");

INSERT INTO Scores(StudentID, SubjectID, Score1, Score2)
VALUES
	("ST0002", "SU0001", 80, 85),
	("ST0002", "SU0002", 85, 85),
	("ST0002", "SU0003", 75, 80),
	("ST0003", "SU0001", 75, 75),
	("ST0003", "SU0002", 85, 80),
	("ST0003", "SU0003", 85, 80);
