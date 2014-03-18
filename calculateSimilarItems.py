from recommendations import *
from sim_distance import *
from topMatches import *
def calculateSimilarItems(prefs,n=10):
	result={}

	itemPrefs=transformPrefs(prefs)
	c=0
	for item in itemPrefs:
		c+=1
		if c%10==00: print "%d / %d" %(c, len(itemPrefs))
		scores=topMatches(itemPrefs, item, n=n, similarity=sim_distance)
		result[item]=scores

	return result
