import numpy as np
import pandas as pd
import pandas
import random
import os
from tqdm import tqdm

def main():
	playerPath = 'player.csv'
	coachPath = 'coach.csv'
	teamPath = 'team.csv'
	coachSeasonStatPath = 'coach_season_stat.csv'
	gamePath = 'game.csv'
	teamYearPath = 'team_year.csv'
	playerYearPath = 'player_year.csv'
	playerSeasonStatPath = 'player_season_stat.csv'
	teamSeasonStatPath = 'team_season_stat.csv'
	teamGameStatPath = 'team_game_stat.csv'
	playerGameStatPath = 'player_game_stat.csv'
	if not os.path.exists(playerPath):
		CreatePlayerCSV(playerPath)
	if not os.path.exists(coachPath):
		CreateCoachCSV(coachPath)
	if not os.path.exists(teamPath):
		CreateTeamCSV(teamPath)
	if not os.path.exists(coachSeasonStatPath):
		CreateCoachSeasonStatCSV(coachSeasonStatPath, coachPath)
	if not os.path.exists(gamePath):
		CreateGameCSV(gamePath, teamPath)
	if not os.path.exists(teamYearPath):
		CreateTeamYearCSV(teamYearPath, coachSeasonStatPath, teamPath)
	if not os.path.exists(playerYearPath):
		CreatePlayerYearCSV(playerYearPath, playerPath, teamPath)
	if not os.path.exists(playerSeasonStatPath):
		CreatePlayerSeasonStatCSV(playerSeasonStatPath, playerYearPath)
	if not os.path.exists(teamSeasonStatPath):
		CreateTeamSeasonStatCSV(teamSeasonStatPath, teamYearPath)
	if not os.path.exists(teamGameStatPath):
		CreateTeamGameStatCSV(teamGameStatPath, teamYearPath)
	if not os.path.exists(playerGameStatPath):
		CreatePlayerGameStatCSV(playerGameStatPath, playerYearPath)

def CreatePlayerGameStatCSV(path, playerYearPath):
	dict={'Player_ID':np.array([]),'Year':np.array([]),
		'Week':np.array([]),'C_ATT':np.array([]),
		'Yards':np.array([]),'Average':np.array([]),
		'Touchdowns':np.array([]),'Interceptions':np.array([]),
		'Quarterback_Rating':np.array([]),'Carries':np.array([]),
		'Long':np.array([]),'Receptions':np.array([]),
		'NO_A':np.array([]),'Field_Goals':np.array([]),
		'Percent':np.array([]),'XP':np.array([]),
		'Points':np.array([]),'Touchback':np.array([]),
		'In_20':np.array([]),'Fumbles':np.array([]),
		'Lost':np.array([]),'TOT':np.array([]),
		'Solo':np.array([]),'Sacks':np.array([]),
		'TFL':np.array([]),'Passes_Defended':np.array([]),
		'Quarterback_Hurries':np.array([])}
	pyDF = pd.read_csv(playerYearPath)
	weeks = [1,2]
	for i in tqdm(range(pyDF.shape[0])):
		py = pyDF.iloc[i]
		for week in weeks:
			dict['Player_ID']=np.append(dict['Player_ID'],py.loc['Player_ID'])
			dict['Year']=np.append(dict['Year'],py.loc['Year'])
			dict['Week']=np.append(dict['Week'],week)
			cAtt = random.randint(0, 25)
			dict['C_ATT']=np.append(dict['C_ATT'],cAtt)
			yards = random.randint(50, 250)
			dict['Yards']=np.append(dict['Yards'],yards)
			average = random.randint(25, 35)
			dict['Average']=np.append(dict['Average'],average)
			tds = random.randint(0,3)
			dict['Touchdowns']=np.append(dict['Touchdowns'],tds)
			ints = random.randint(0,2)
			dict['Interceptions']=np.append(dict['Interceptions'],ints)
			qbr = random.randint(70,250) + 0.36
			dict['Quarterback_Rating']=np.append(dict['Quarterback_Rating'],qbr)
			carries = random.randint(0, 25)
			dict['Carries']=np.append(dict['Carries'],carries)
			long = random.randint(15, 75)
			dict['Long']=np.append(dict['Long'],long)
			recps = random.randint(1,15)
			dict['Receptions']=np.append(dict['Receptions'],recps)
			noA = random.randint(0,3)
			dict['NO_A']=np.append(dict['NO_A'],noA)
			fieldGoals = random.randint(0,tds)
			dict['Field_Goals']=np.append(dict['Field_Goals'],0)
			dict['Percent']=np.append(dict['Percent'],1.0)
			dict['XP']=np.append(dict['XP'],tds)
			dict['Points']=np.append(dict['Points'],tds * 7)
			dict['Touchback']=np.append(dict['Touchback'],0)
			in20 = random.randint(0, 10)
			dict['In_20']=np.append(dict['In_20'],in20)
			dict['Fumbles']=np.append(dict['Fumbles'],0)
			dict['Lost']=np.append(dict['Lost'],0)
			tackles = random.randint(0,7)
			dict['TOT']=np.append(dict['TOT'],tackles)
			solo = random.randint(0,tackles)
			dict['Solo']=np.append(dict['Solo'],solo)
			sacks = random.randint(0,3)
			dict['Sacks']=np.append(dict['Sacks'],sacks)
			tfl = random.randint(0,tackles - solo)
			dict['TFL']=np.append(dict['TFL'],tfl)
			passD = random.randint(0, 20)
			dict['Passes_Defended']=np.append(dict['Passes_Defended'],passD)
			qbH = random.randint(0, 10)
			dict['Quarterback_Hurries']=np.append(dict['Quarterback_Hurries'],qbH)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)	

def CreateTeamGameStatCSV(path, teamYearPath):
	dict={'Team_ID':np.array([]),'Year':np.array([]),
		'Week':np.array([]),'Points':np.array([]),
		'Home_Away':np.array([]),'Fumbles_Recovered':np.array([]),
		'Rushing_Touchdowns':np.array([]),
		'Passing_Touchdowns':np.array([]),
		'Kick_Return_Yards':np.array([]),
		'Kick_Return_Touchdowns':np.array([]),
		'Kick_Returns':np.array([]),'Kicking_Points':np.array([]),
		'First_Downs':np.array([]),
		'Third_Down_Efficiency':np.array([]),
		'Fourth_Down_Efficiency':np.array([]),
		'Total_Yards':np.array([]),'Net_Passing_Yards':np.array([]),
		'Completion_Attempts':np.array([]),'Yards_Per_Pass':np.array([]),
		'Rushing_Attempts':np.array([]),'Rushing_Yards':np.array([]),
		'Yards_Per_Rush_Attempt':np.array([]),
		'Total_Penalty_Yards':np.array([]),'Turnovers':np.array([]),
		'Fumbles_Lost':np.array([]),'Interceptions':np.array([]),
		'Possession_Time':np.array([]),
		'Punt_Return_Yards':np.array([]),
		'Punt_Return_Touchdowns':np.array([]),
		'Punt_Returns':np.array([]),'Interception_Yards':np.array([]),
		'Interception_Touchdowns':np.array([]),
		'Passes_Intercepted':np.array([]),'Total_Fumbles':np.array([]),
		'Tackles_For_Loss':np.array([]),
		'Defensive_Touchdowns':np.array([]),
		'Tackles':np.array([]),'Sacks':np.array([]),
		'QB_Hurries':np.array([]),'Passes_Deflected':np.array([])
		}
	tyDF = pd.read_csv(teamYearPath)
	weeks = [1,2]
	for i in tqdm(range(tyDF.shape[0])):
		ty = tyDF.iloc[i]
		for week in weeks:
			dict['Team_ID']=np.append(dict['Team_ID'],ty.loc['Team_ID'])
			dict['Year']=np.append(dict['Year'],ty.loc['Year'])
			dict['Week']=np.append(dict['Week'],week)
			tds = random.randint(0,5)
			dict['Points']=np.append(dict['Points'],tds*7)
			homeAway = random.randint(0,1)
			dict['Home_Away']=np.append(dict['Home_Away'],homeAway)
			fumblesRec = random.randint(0,3)
			dict['Fumbles_Recovered']=np.append(dict['Fumbles_Recovered'],fumblesRec)
			rushingTds = random.randint(0,tds)
			dict['Rushing_Touchdowns']=np.append(dict['Rushing_Touchdowns'],rushingTds)
			passingTds = random.randint(0,tds - rushingTds)
			dict['Passing_Touchdowns']=np.append(dict['Passing_Touchdowns'], passingTds)
			kickRetYds = random.randint(0, 100)
			dict['Kick_Return_Yards']=np.append(dict['Kick_Return_Yards'],kickRetYds)
			dict['Kick_Return_Touchdowns']=np.append(dict['Kick_Return_Touchdowns'],0)
			kickRet = random.randint(0, 5)
			dict['Kick_Returns']=np.append(dict['Kick_Returns'],kickRet)
			dict['Kicking_Points']=np.append(dict['Kicking_Points'],tds)
			fd = random.randint(0, 13)
			dict['First_Downs']=np.append(dict['First_Downs'],fd)
			tde = random.randint(0, 13) / 13
			dict['Third_Down_Efficiency']=np.append(dict['Third_Down_Efficiency'],tde)
			fde = random.randint(0,3) /3
			dict['Fourth_Down_Efficiency']=np.append(dict['Fourth_Down_Efficiency'],fde)
			yards = random.randint(0, 330)
			dict['Total_Yards']=np.append(dict['Total_Yards'], yards)
			netPassYards = random.randint(0, yards)
			dict['Net_Passing_Yards']=np.append(dict['Net_Passing_Yards'], netPassYards)
			compl = random.randint(0,35)
			dict['Completion_Attempts']=np.append(dict['Completion_Attempts'],compl)
			dict['Yards_Per_Pass']=np.append(dict['Yards_Per_Pass'],netPassYards / (compl + 10))
			rushAtt = random.randint(1,35)
			dict['Rushing_Attempts']=np.append(dict['Rushing_Attempts'], rushAtt)
			rushYrd = yards - netPassYards
			dict['Rushing_Yards']=np.append(dict['Rushing_Yards'],rushYrd)
			dict['Yards_Per_Rush_Attempt']=np.append(dict['Yards_Per_Rush_Attempt'], (yards - netPassYards) / rushAtt)
			penYrd = random.randint(0,13)
			dict['Total_Penalty_Yards']=np.append(dict['Total_Penalty_Yards'],penYrd * 5)
			turnovers = random.randint(0, 5)
			dict['Turnovers']=np.append(dict['Turnovers'],turnovers)
			fumbLost = random.randint(0, 3)
			dict['Fumbles_Lost']=np.append(dict['Fumbles_Lost'],fumbLost)
			interceptions = random.randint(0, 3)
			dict['Interceptions']=np.append(dict['Interceptions'],interceptions)
			possTime = random.randint(25,75)/100
			dict['Possession_Time']=np.append(dict['Possession_Time'],possTime)
			dict['Punt_Return_Yards']=np.append(dict['Punt_Return_Yards'],0)
			dict['Punt_Return_Touchdowns']=np.append(dict['Punt_Return_Touchdowns'],0)
			dict['Punt_Returns']=np.append(dict['Punt_Returns'],0)
			dict['Interception_Yards']=np.append(dict['Interception_Yards'],0)
			dict['Interception_Touchdowns']=np.append(dict['Interception_Touchdowns'],0)
			pi = random.randint(0, 2)
			dict['Passes_Intercepted']=np.append(dict['Passes_Intercepted'],pi)
			totFum = random.randint(0,3)
			dict['Total_Fumbles']=np.append(dict['Total_Fumbles'],totFum)
			tfl = random.randint(0,10)
			dict['Tackles_For_Loss']=np.append(dict['Tackles_For_Loss'],tfl)
			dfsTds = tds - rushingTds - passingTds
			dict['Defensive_Touchdowns']=np.append(dict['Defensive_Touchdowns'],dfsTds)
			tackles = random.randint(tfl, tfl + 15)
			dict['Tackles']=np.append(dict['Tackles'],tackles)
			sacks = random.randint(0, 3)
			dict['Sacks']=np.append(dict['Sacks'],sacks)
			qbHurry = random.randint(0,10)
			dict['QB_Hurries']=np.append(dict['QB_Hurries'],qbHurry)
			passesDef = random.randint(0,5)
			dict['Passes_Deflected']=np.append(dict['Passes_Deflected'],passesDef)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)
			
def CreateTeamSeasonStatCSV(path, teamYearPath):
	dict={'Team_ID':np.array([]),'Year':np.array([]),
		'Touchdowns':np.array([]),'Long':np.array([]),
		'Receptions':np.array([]),'NO_A':np.array([]),
		'Yards_Per_Reception':np.array([]),'Average':np.array([]),
		'Attempts':np.array([]),'Percent':np.array([]),
		'Yards_Per_Pass':np.array([]),'Completions':np.array([]),
		'Touchback':np.array([]),'XPM':np.array([]),
		'Inside_20':np.array([]),'Field_Goal_Attempts':np.array([]),
		'Passes_Defended':np.array([]),'QB_Hurries':np.array([]),
		'TFL':np.array([]),'TOT':np.array([]),
		'Solo':np.array([]),'Sack':np.array([]),
		'Fumble':np.array([]),'Lost':np.array([]),
		'Lost':np.array([])}
	tyDF = pd.read_csv(teamYearPath)
	for i in tqdm(range(tyDF.shape[0])):
		ty = tyDF.iloc[i]
		dict['Team_ID']=np.append(dict['Team_ID'],ty.loc['Team_ID'])
		dict['Year']=np.append(dict['Year'],ty.loc['Year'])
		tds = random.randint(5, 20)
		dict['Touchdowns']=np.append(dict['Touchdowns'],tds)
		lng = random.randint(50, 100)
		dict['Long']=np.append(dict['Long'],lng)
		recp = random.randint(150,300)
		dict['Receptions']=np.append(dict['Receptions'],recp)
		noA = random.randint(0, 5)
		dict['NO_A']=np.append(dict['NO_A'],noA)
		ydsPerRec = random.randint(5, 35)
		dict['Yards_Per_Reception']=np.append(dict['Yards_Per_Reception'],ydsPerRec)
		average = random.randint(0,25)
		dict['Average']=np.append(dict['Average'],average)
		attempts = random.randint(recp,recp+100)
		dict['Attempts']=np.append(dict['Attempts'],attempts)
		dict['Percent']=np.append(dict['Percent'],recp/attempts)
		ydsPerPass = ydsPerRec * recp / attempts
		dict['Yards_Per_Pass']=np.append(dict['Yards_Per_Pass'],ydsPerPass)
		dict['Completions']=np.append(dict['Completions'],recp)
		touchback = random.randint(0, 5)
		dict['Touchback']=np.append(dict['Touchback'],touchback)
		xpm = random.randint(0,tds)
		dict['XPM']=np.append(dict['XPM'],xpm)
		inside20 = random.randint(25,50)
		dict['Inside_20']=np.append(dict['Inside_20'],inside20)
		fieldGoalAtt = random.randint(5, 25)
		dict['Field_Goal_Attempts']=np.append(dict['Field_Goal_Attempts'],fieldGoalAtt)
		passesDef = random.randint(100, 150)
		dict['Passes_Defended']=np.append(dict['Passes_Defended'],passesDef)
		qbHurries = random.randint(50,75)
		dict['QB_Hurries']=np.append(dict['QB_Hurries'],qbHurries)
		tfl = random.randint(20,50)
		dict['TFL']=np.append(dict['TFL'],tfl)
		tot = random.randint(100,205)
		dict['TOT']=np.append(dict['TOT'],tot)
		solo = random.randint(50,tot)
		dict['Solo']=np.append(dict['Solo'],solo)
		sack = random.randint(10,50)
		dict['Sack']=np.append(dict['Sack'],sack)
		fumb = random.randint(0,10)
		dict['Fumble']=np.append(dict['Fumble'],fumb)
		lost = random.randint(0,8)
		dict['Lost']=np.append(dict['Lost'],lost)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreatePlayerSeasonStatCSV(path, playerYearPath):
	dict = {'Player_ID':np.array([]),'Year':np.array([]),
		'Touchdowns':np.array([]),'Long':np.array([]),
		'Receptions':np.array([]),'NO_A':np.array([]),
		'Yards_Per_Carry':np.array([]),'Carries':np.array([]),
		'Interceptions':np.array([]),'Yards_Per_Reception':np.array([]),
		'Average':np.array([]),'Attempts':np.array([]),
		'Percent':np.array([]),'Yards_Per_Pass':np.array([]),
		'Completions':np.array([]),'Touchback':np.array([]),
		'XPM':np.array([]),'In_20':np.array([]),
		'Field_Goal_Attempts':np.array([]),'Points':np.array([]),
		'XPA':np.array([]),'Field_Goal_Made':np.array([]),
		'PD':np.array([]),'QB_Hurries':np.array([]),
		'TFL':np.array([]),'TOT':np.array([]),
		'Solo':np.array([]),'Sack':np.array([]),
		'Fumble':np.array([]),'Lost':np.array([])}
	
	pyDF = pd.read_csv(playerYearPath)
	
	for i in tqdm(range(pyDF.shape[0])):
		py = pyDF.iloc[i]
		dict['Player_ID']=np.append(dict['Player_ID'],py.loc['Player_ID'])
		dict['Year']=np.append(dict['Year'],py.loc['Year'])
		tds = random.randint(0, 5)
		dict['Touchdowns']=np.append(dict['Touchdowns'],tds)
		long = random.randint(25,100)
		dict['Long']=np.append(dict['Long'],long)
		recs = random.randint(5,130)
		dict['Receptions']=np.append(dict['Receptions'],recs)
		noA = random.randint(10,20)
		dict['NO_A']=np.append(dict['NO_A'],noA)
		ydsPerCarry = random.randint(2, 10)
		dict['Yards_Per_Carry']=np.append(dict['Yards_Per_Carry'],ydsPerCarry)
		carries = random.randint(50, 250)
		dict['Carries']=np.append(dict['Carries'],carries)
		interceptions = random.randint(5, 15)
		dict['Interceptions']=np.append(dict['Interceptions'],interceptions)
		ydsPerRec = random.randint(5, 50)
		dict['Yards_Per_Reception']=np.append(dict['Yards_Per_Reception'],ydsPerRec)
		average = random.randint(2,20)
		dict['Average']=np.append(dict['Average'],average)
		attempts = random.randint(2,250)
		dict['Attempts']=np.append(dict['Attempts'],attempts)
		completions = random.randint(0,attempts)
		dict['Percent']=np.append(dict['Percent'],completions/attempts)
		ydsPerPass = random.randint(2,25)
		dict['Yards_Per_Pass']=np.append(dict['Yards_Per_Pass'],ydsPerPass)
		dict['Completions']=np.append(dict['Completions'],completions)
		touchbacks = random.randint(0,3)
		dict['Touchback']=np.append(dict['Touchback'],touchbacks)
		XPM = random.randint(0,tds)
		dict['XPM']=np.append(dict['XPM'],XPM)
		In_20 = random.randint(0,25)
		dict['In_20']=np.append(dict['In_20'],In_20)
		fieldGoalAttempts = random.randint(0, 15)
		dict['Field_Goal_Attempts']=np.append(dict['Field_Goal_Attempts'],fieldGoalAttempts)
		fieldGoalMade = random.randint(0,fieldGoalAttempts)
		points = tds * 6 + XPM + fieldGoalMade * 3
		dict['Points']=np.append(dict['Points'],points)
		xpa = random.randint(XPM, tds)
		dict['XPA']=np.append(dict['XPA'], xpa)
		dict['Field_Goal_Made']=np.append(dict['Field_Goal_Made'],fieldGoalMade)
		pdVar = random.randint(0, 10)
		dict['PD']=np.append(dict['PD'],pdVar)
		qbHurries = random.randint(0, 30)
		dict['QB_Hurries']=np.append(dict['QB_Hurries'],qbHurries)
		tfl = random.randint(0, 30)
		dict['TFL']=np.append(dict['TFL'],tfl)
		tot = random.randint(0,30)
		dict['TOT']=np.append(dict['TOT'],tot)
		solo = random.randint(0, tot)
		dict['Solo']=np.append(dict['Solo'],solo)
		sack = random.randint(0, 15)
		dict['Sack']=np.append(dict['Sack'],sack)
		fumble = random.randint(0,5)
		dict['Fumble']=np.append(dict['Fumble'],fumble)
		lost = random.randint(0,5)
		dict['Lost']=np.append(dict['Lost'],lost)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreatePlayerYearCSV(path, playerPath, teamPath):
	dict={'Player_ID':np.array([]),'Year':np.array([]),
		'Age':np.array([]),'Height':np.array([]),
		'Weight':np.array([]),'Team_ID':np.array([])}
	pDF = pd.read_csv(playerPath)
	print(pDF.ID.unique())
	tDF = pd.read_csv(teamPath)
	years=[2023,2024]
	for i in tqdm(range(pDF.shape[0])):
		p = pDF.iloc[i]
		for year in years:
			dict['Player_ID']=np.append(dict['Player_ID'],p.loc['ID'])
			dict['Year']=np.append(dict['Year'],year)
			if year == 2023:
				dict['Age']=np.append(dict['Age'],20)
			else:
				dict['Age']=np.append(dict['Age'],21)
			height = random.randint(65, 74)
			weight = random.randint(120, 210)
			dict['Height']=np.append(dict['Height'],height)
			dict['Weight']=np.append(dict['Weight'],weight)
			dict['Team_ID']=np.append(dict['Team_ID'],p.loc['ID'])
	df = pd.DataFrame.from_dict(dict)
	df.Player_ID = df.Player_ID.astype(int)
	df.Team_ID = df.Team_ID.astype(int)
	df.to_csv(path, index=False)

def CreateTeamYearCSV(path, coachSeasonStatPath, teamPath):
	dict={'Team_ID':np.array([]),'Year':np.array([]),
		'Coach_ID':np.array([]),'Conference':np.array([])}
	cssDF = pd.read_csv(coachSeasonStatPath)
	teamDF = pd.read_csv(teamPath)
	for i in tqdm(range(cssDF.shape[0])):
		css = cssDF.iloc[i]
		dict['Team_ID']=np.append(dict['Team_ID'], css.loc['Coach_ID'])
		dict['Year']=np.append(dict['Year'], css.loc['Year'])
		dict['Coach_ID']=np.append(dict['Coach_ID'], css.loc['Coach_ID'])
		dict['Conference']=np.append(dict['Conference'], '')
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreateGameCSV(path, teamPath):
	dict={'ID':np.array([]),'Year':np.array([]),
		'Week':np.array([]),'Season_Type':np.array([]),
		'Home_Team_ID':np.array([]),'Away_Team_ID':np.array([]),
		'Home_Points':np.array([]),'Away_Points':np.array([])}
	teamDF = pd.read_csv(teamPath)
	teamIDs = teamDF.ID
	years=[2023,2024]
	weeks=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	seasonTypes=[0,0,0,0,0,1]
	for i in tqdm(range(20)):
		dict['ID']=np.append(dict['ID'], dict['ID'].shape[0])
		dict['Year']=np.append(dict['Year'], 2023)
		dict['Week']=np.append(dict['Week'], random.choice(weeks))
		dict['Season_Type']=np.append(dict['Season_Type'], random.choice(seasonTypes))
		homeTeamID = random.choice(teamIDs)
		awayTeamID = random.choice(teamIDs)
		while homeTeamID == awayTeamID:
			awayTeamID = random.choice(teamIDs)
		dict['Home_Team_ID']=np.append(dict['Home_Team_ID'], homeTeamID)
		dict['Away_Team_ID']=np.append(dict['Away_Team_ID'], awayTeamID)
		homePoints = random.randint(0, 5) * 7
		awayPoints = random.randint(0, 5) * 7
		dict['Home_Points']=np.append(dict['Home_Points'], homePoints)
		dict['Away_Points']=np.append(dict['Away_Points'], awayPoints)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreateCoachSeasonStatCSV(path, coachPath):
	dict={'Coach_ID':np.array([]),'Year':np.array([]),
		'Wins':np.array([]),'Losses':np.array([]),
		'Num_Passes':np.array([]), 'Num_Runs':np.array([])}
	coachDF = pd.read_csv(coachPath)
	years=[2022,2023]
	for i in tqdm(range(coachDF.shape[0])):
		coach = coachDF.iloc[i]
		for year in years:
			dict['Coach_ID']=np.append(dict['Coach_ID'], coach.loc['ID'])
			dict['Year']=np.append(dict['Year'],year)
			dict['Wins']=np.append(dict['Wins'],7)
			dict['Losses']=np.append(dict['Losses'],7)
			passes = random.randint(0, 100)
			dict['Num_Passes']=np.append(dict['Num_Passes'],passes)
			dict['Num_Runs']=np.append(dict['Num_Runs'],100-passes)
	df = pd.DataFrame.from_dict(dict)
	df.Coach_ID = df.Coach_ID.astype(int)
	df.to_csv(path, index=False)

def CreateTeamCSV(path):
	dict={'ID':np.array([]),'Name':np.array([])}
	teams=['Alabama Crimson Tide','Arkansas Razorbacks',
		'Auburn Tigers', 'Florida Gators',
		'Georgia Bulldogs', 'Kentucky Wildcats',
		'LSU Tigers', 'Mississippi State Bulldogs',
		'Missouri Tigers', 'Ole Miss Rebels',
		'South Carolina Gamecocks', 'Tennessee Volunteers',
		'Texas A&M Aggies', 'Vanderbilt Commodores',
		'Ohio State Buckeyes', 'Indiana Hoosiers',
		'Iowa Hawkeyes', 'Maryland Terrapins',
		'Michigan State Spartans', 'Michigan Wolverines']
	print('CREATING TEAMS DATASETS')
	for i in tqdm(range(20)):
		dict['ID']=np.append(dict['ID'], i)
		dict['Name']=np.append(dict['Name'], teams[i])
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreateCoachCSV(path):
	dict = {'ID':np.array([]),'Name':np.array([])}
	first=['Johnathan','Joseph','Bobby','Alan','Albert','Micheal','James',
		'David','Richard','William','Thomas','Christopher']
	last=['Walker','Lewis','Young','Allen','King','Wright','Scott','Torres',
		'Hill','Flores','Green','Adams','Nelson','Baker','Hall']
	print('CREATING COACH DATASET')
	for i in tqdm(range(20)):
		dict['ID']=np.append(dict['ID'], i)
		temp = random.choice(first) + ' ' + random.choice(last)
		dict['Name']=np.append(dict['Name'], temp)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

def CreatePlayerCSV(path):
	dict = {'ID':np.array([]),'Name':np.array([])}
	firstNames = ['John','Joe','Bob','Alan','Lance','Albert','Mike','Nick']
	lastNames = ['Smith','Johnson','Williams','Brown','Jones','Garcia',
	'Miller','Davis','Wilson','Anderson','Thomas','Taylor']
	print('CREATING PLAYER DATASET')
	for i in tqdm(range(20)):
		dict['ID'] = np.append(dict['ID'], i)
		madeName = random.choice(firstNames) + ' ' + random.choice(lastNames)
		dict['Name'] = np.append(dict['Name'], madeName)
	df = pd.DataFrame.from_dict(dict)
	df.to_csv(path, index=False)

main()
