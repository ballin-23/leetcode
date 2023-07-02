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
            print("home team")
            if competitions[count][0] in team_scores:
                team_scores[competitions[count][0]] += 3
            else:
                team_scores[competitions[count][0]] = 3
        else:
            print("away team")
            if competitions[count][1] in team_scores:
                team_scores[competitions[count][1]] += 3
            else:
                team_scores[competitions[count][1]] = 3
        count += 1
    max = float('-inf')
    high = ""
    for team in team_scores:
        if team_scores[team] > max:
            max = team_scores[team]
            high = team
    print(max, high)
    return team

# competitions = [["html", "c#"], ["c#", "python"], ["python", "html"]]
competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"]
  ]
results = [0,1,1]

tournament_winner(competitions, results)



    
