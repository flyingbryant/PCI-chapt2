from recommendations import critics
from sim_distance import sim_pearson

def getRecommendations(prefs, person, similarity = sim_pearson):
	totals = {}
	simSums = {}

	for other in prefs:
		if other == person: continue
		sim = similarity(prefs, person, other)

		if sim<=0: continue
		for item in prefs[other]:
			if item not in prefs[person] or prefs[person][item]==0:
				totals.setdefault(item,0)
				totals[item] += prefs[other][item] * sim
				simSums.setdefault(item, 0)
				simSums[item]+=sim

	rankings = [(total/simSums[item], item) for item, total in totals.items()]

	rankings.sort()
	rankings.reverse()
	return rankings



def getRecommendedItems(prefs, itemMatch, user):
	userRatings=prefs[user]
	scores={}
	totalSim={}

	for(item,rating) in userRatings.items():
		for(similarity,item2) in itemMatch[item]:
			if item2 in userRatings: continue
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating

			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity

	rankings=[(score/totalSim[item],item) for item ,score in scores.items()]

	rankings.sort()
	rankings.reverse()
	return rankings
	

