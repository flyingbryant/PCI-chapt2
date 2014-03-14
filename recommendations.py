# A dictionary of movie critics and their ratings of a small set of movies
from math import sqrt

person={'Lisa Rose', 'Gene Seymour', 'Micheal Phillips', 'Claudia Puig', 'Mick LaSalle', 'Jack Matthews', 'Toby'}
critics={'Lisa Rose':{'Lady in the Water':2.5, 'Snake on a Plane':3.5, 'Just My Luck':3.0, 'Superman Returns':3.5, 'You, Me and Dupree':2.5, 'The Night Listener':3.0},
'Gene Seymour':{'Lady in the Water':3.0, 'Snake on a Plane':3.5, 'Just My Luck':1.5, 'Superman Returns':5.0, 'The Night Listener':3.0, 'You, Me and Dupree':3.5},
'Micheal Phillips':{'Lady in the Water':2.5, 'Snake on a Plane':3.0, 'Superman Returns':3.5, 'The Night Listener':4.0},
'Claudia Puig':{'Snake on a Plane':3.5, 'Just My Luck':3.0, 'The Night Listener':4.5, 'Superman Returns':4.0, 'You, Me and Dupree':2.5},
'Mick LaSalle':{'Lady in the Water':3.0, 'Snake on a Plane':4.0, 'Just My Luck':2.0, 'Superman Returns':3.0, 'The Night Listener':3.0, 'You, Me and Dupree':2.0},
'Jack Matthews':{'Lady in the Water':3.0, 'Snake on a Plane':4.0, 'The Night Listener':3.0, 'Superman Returns':5.0, 'You, Me and Dupree':3.5},
'Toby':{'Snake on a Plane':4.5, 'Superman Returns':4.0, 'You, Me and Dupree':1.0}}

def sim_distance(prefs,person1,person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1

	if len(si)==0: return 0
	sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2)
				     for item in prefs[person1] if item in prefs[person2]])

	return 1/(1+sum_of_squares)


def most_in_common():
	maxValue = 0
	for person1 in person:
		for person2 in person:
			if person1 != person2:
				answer = sim_distance(critics, person1, person2)
				if answer > maxValue:
					maxValue = answer
					targetPer1 = person1
					targetPer2 = person2
	
	print "%s and %s have the most in common, the similarity is %r" %(targetPer1, targetPer2, maxValue)

def transformPrefs(prefs):
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			result[item][person] = prefs[person][item]

	return result


