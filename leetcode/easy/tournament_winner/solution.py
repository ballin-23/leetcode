# determine who the tournament winner is
# [hometeam, awayteam]
# competitions => 1 in the results array means that the home team one and a 0 means the away team one

# algorithm: 
# figure out what structure to store results in => dictionary => key = name of team

def tournament_winner(competitions, results):
    team_scores = {}
    count = 0
    while count < len(competitions):
        winner = results[count]
        if winner == 1:
            team_scores = update_dictionary(0,team_scores, competitions, count)
        else:
            team_scores = update_dictionary(1,team_scores, competitions, count)
        count += 1
    return calculate_max(team_scores)

def update_dictionary(index, team_scores, competitions, count):
    if competitions[count][index] in team_scores:
        team_scores[competitions[count][index]] += 3
    else:
        team_scores[competitions[count][index]] = 3
    return team_scores

def calculate_max(team_scores):
    max = float('-inf')
    team_with_highest_score = ""
    for team in team_scores:
        if team_scores[team] > max:
            max = team_scores[team]
            team_with_highest_score = team
    return team_with_highest_score


competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
  ]
results = [0,1,1]

print(tournament_winner(competitions, results))



    
