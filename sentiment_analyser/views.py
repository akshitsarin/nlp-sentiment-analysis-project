from django.shortcuts import render
from django.http import HttpResponse

from .models import Reviews

def review_view(request, *args, **keywordargs):
	return render(request, 'review.html', {})

def review_added_view(request, *args, **keywordargs):
	name = request.POST.get('name')
	# if review is positive, add to positive

	# if review is negative, add to negative

	return render(request, 'review_added.html', {})
	
def ratings_view(request, *args, **keywordargs):
	ratings = {}

	# queen ratings
	queen_pos = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Queen" AND positive > 0'):
		queen_pos += 1

	queen_neg = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Queen" AND negative > 0'):
		queen_neg += 1

	# ek tha tiger ratings
	tiger_pos = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Ek Tha Tiger" AND positive > 0'):
		tiger_pos += 1

	tiger_neg = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Ek Tha Tiger" AND negative > 0'):
		tiger_neg += 1

	# joker ratings
	joker_pos = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Joker" AND positive > 0'):
		joker_pos += 1

	joker_neg = 0
	for i in Reviews.objects.raw('SELECT * FROM sentiment_analyser_reviews WHERE name="Joker" AND negative > 0'):
		joker_neg += 1

	# add to ratings dict
	ratings['queen'] = queen_neg + queen_pos
	if ratings['queen'] == 0:
		ratings['queen_pos'] = ratings['queen_neg'] = 0
	else:
		ratings['queen_pos'] = round((queen_pos / ratings['queen']) * 100, 2)
		ratings['queen_neg'] = round((queen_neg / ratings['queen']) * 100, 2)

	ratings['tiger'] = tiger_neg + tiger_pos
	if ratings['tiger'] == 0:
		ratings['tiger_pos'] = ratings['tiger_neg'] = 0
	else:
		ratings['tiger_pos'] = round((tiger_pos / ratings['tiger']) * 100, 2)
		ratings['tiger_neg'] = round((tiger_neg / ratings['tiger']) * 100, 2)

	ratings['joker'] = joker_neg + joker_pos
	if ratings['joker'] == 0:
		ratings['joker_pos'] = ratings['joker_neg'] = 0
	else:
		ratings['joker_pos'] = round((joker_pos / ratings['joker']) * 100, 2)
		ratings['joker_neg'] = round((joker_neg / ratings['joker']) * 100, 2)

	# pos % = round((pos / (pos + neg)) * 100, 2)
	
	return render(request, 'ratings.html', ratings)