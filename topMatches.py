from sim_distance import sim_pearson

def topMatches(prefs, person, n=5, similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other)
			for other in prefs if other != person]

	scores.sort()
	scores.reverse()
	return scores[0:n]

