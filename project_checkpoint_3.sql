--
-- File generated with SQLiteStudio v3.4.4 on Mon Jun 24 19:07:05 2024
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: PLAYER
create table if not exists PLAYER (
	ID int not null,
	Name varchar(100),
	primary key (ID)
);

-- Table: COACH
create table if not exists COACH (
	ID int not null,
	Name varchar (100),
	Primary Key (ID)
);

-- Table: TEAM
create table if not exists TEAM (
	ID int not null,
	Name varchar(100),
	primary key (ID)
);

-- Table: COACH_SEASON_STAT
create table if not exists COACH_SEASON_STAT (
	Coach_ID int not null,
	Year int not null,
	Wins int,
	Losses int,
	Num_Passes int,
	Num_Runs int,
	primary key (Coach_ID, Year),
	foreign key (Coach_ID) references COACH (ID)
);

-- Table: GAME
create table if not exists GAME (
	ID int NOT NULL, 
	Year int NOT NULL, 
	Week int NOT NULL, 
	Season_Type int, 
	Home_Team_ID int NOT NULL, 
	Away_Team_ID int NOT NULL, 
	Home_Points int, 
	Away_Points int, 
	primary key (ID), 
	foreign key (Home_Team_ID) REFERENCES TEAM (ID), 
	foreign key (Away_Team_ID) REFERENCES TEAM (ID)
);

-- Table: PLAYER_GAME_STATS
create table if not exists PLAYER_GAME_STATS (
	Player_ID int not null,
	Year int not null,
	Week int not null,
	C_ATT int,
	Yards int,
	Average int,
	Touchdowns int,
	Interceptions int,
	Quarterback_Rating float8,
	Carries int,
	Long int,
	Receptions int,
	NO_A int,
	Field_Goals int,
	Percent float8,
	XP int,
	Points int,
	Touchback int,
	In_20 int,
	Fumbles int,
	Lost int,
	TOT int,
	Solo int,
	Sacks int,
	TFL int,
	Passes_Defended int,
	Quarterback_Hurries int,
	primary key (Player_ID, Year, Week),
	foreign key (Player_ID) references PLAYER (ID)
);

-- Table: PLAYER_SEASON_STATS
create table if not exists PLAYER_SEASON_STATS(
	Player_ID int NOT NULL,
	Year int NOT NULL,
	Touchdowns int,
	Long int,
	Receptions int,
	NO_A int,
	Yards_Per_Carry int,
	Carries int,
	Interceptions int,
	Yards_Per_Reception int,
	Average int,
	Attempts int,
	Percent float8,
	Yards_Per_Pass int,
	Completions int,
	Touchback int,
	XPM int,
	In_20 int,
	Field_Goal_Attempts int,
	Points int,
	XPA int,
	Field_Goal_Made int,
	PD int,
	QB_Hurries int,
	TFL int,
	TOT int,
	Solo int,
	Sack int,
	Fumble int,
	Lost int,
	primary key (Player_ID, Year),
	foreign key (Player_ID) references PLAYER (ID)
);

-- Table: PLAYER_YEAR
create table if not exists PLAYER_YEAR (
	Player_ID int not null,
	Year int not null,
	Age int,
	Height int,
	Weight int,
	Team_ID int not null,
	primary key (Player_ID, Year),
	foreign key (Team_ID) references TEAM (ID),
	foreign key (Player_ID) references PLAYER (ID)
);

-- Table: TEAM_GAME_STATS
create table if not exists TEAM_GAME_STATS (
	Team_ID int not null,
	Year int not null,
	Week int not null,
	Points int,
	Home_Away int,
	Fumbles_Recovered int,
	Rushing_Touchdowns int,
	Passing_Touchdowns int,
	Kick_Return_Yards int,
	Kick_Return_Touchdowns int,
	Kick_Returns int,
	Kicking_Points int,
	First_Downs int,
	Third_Down_Efficiency int,
	Fourth_Down_Efficiency int,
	Total_Yards int,
	Net_Passing_Yards int,
	Completion_Attempts int,
	Yards_Per_Pass int,
	Rushing_Attempts int,
	Rushing_Yards int,
	Yards_Per_Rush_Attempt int,
	Total_Penalty_Yards int,
	Turnovers int,
	Fumbles_Lost int,
	Interceptions int,
	Possession_Time float8,
	Punt_Return_Yards int,
	Punt_Return_Touchdowns int,
	Punt_Returns int,
	Interception_Yards int,
	Interception_Touchdowns int,
	Passes_Intercepted int,
	Total_Fumbles int,
	Tackles_For_Loss int,
	Defensive_Touchdowns int,
	Tackles int,
	Sacks int,
	QB_Hurries int,
	Passes_Deflected int,
	primary key (Team_ID, Year, Week),
	foreign key (Team_ID) references TEAM (ID)
);

-- Table: TEAM_SEASON_STATS
create table if not exists TEAM_SEASON_STATS (
	Team_ID int not null,
	Year int not null,
	Touchdowns int,
	Long int,
	Receptions int,
	NO_A int,
	Yards_Per_Reception int,
	Average int,
	Attempts int,
	Percent float8,
	Yards_Per_Pass int,
	Completions int,
	Touchback int,
	XPM int,
	Inside_20 int,
	Field_Goal_Attempts int,
	Passes_Defended int,
	QB_Hurries int,
	TFL int,
	TOT int,
	Solo int,
	Sack int,
	Fumble int,
	Lost int,
	primary key (Team_ID, Year),
	foreign key (Team_ID) references TEAM (ID)
);

-- Table: TEAM_YEAR
create table if not exists TEAM_YEAR (
	Team_ID int not null,
	Year int not null,
	Coach_ID int not null,
	Conference varchar(100),
	primary key (Team_ID, Year),
	foreign key (Coach_ID) references COACH (ID),
	foreign key (Team_ID) references TEAM (ID)
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
