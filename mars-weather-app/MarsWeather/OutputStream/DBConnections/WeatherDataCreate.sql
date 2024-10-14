CREATE TABLE IF NOT EXISTS sols
(sol INTEGER PRIMARY KEY,
date_retrieved TEXT,
season TEXT,
first_utc TEXT,
last_utc TEXT);

CREATE TABLE IF NOT EXISTS AV
(sol INTEGER PRIMARY KEY,
av REAL,
ct REAL,
mn REAL,
mx REAL,
FOREIGN KEY (sol) REFERENCES sols(sol));

CREATE TABLE IF NOT EXISTS HWS
(sol INTEGER PRIMARY KEY,
av REAL,
ct REAL,
mn REAL,
mx REAL,
FOREIGN KEY (sol) REFERENCES sols(sol));

CREATE TABLE IF NOT EXISTS PRE
(sol INTEGER PRIMARY KEY,
av REAL,
ct REAL,
mn REAL,
mx REAL,
FOREIGN KEY (sol) REFERENCES sols(sol));

CREATE TABLE IF NOT EXISTS compass_pt
(compass_pt_id INTEGER PRIMARY KEY,
sol INTEGER,
compass_degrees REAL,
compass_point TEXT,
compass_right REAL,
compass_up REAL,
FOREIGN KEY (sol) REFERENCES sols(sol));

CREATE TABLE IF NOT EXISTS WD
(sol INTEGER PRIMARY KEY,
most_common INTEGER,
FOREIGN KEY (sol) REFERENCES sols(sol),
FOREIGN KEY (most_common) REFERENCES compass_pt(compass_pt_id)
);