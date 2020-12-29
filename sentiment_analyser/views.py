from django.shortcuts import render
from django.http import HttpResponse

from .models import Reviews
import uuid 
  
def review_view(request, *args, **keywordargs):
	return render(request, 'review.html', {})

def review_added_view(request, *args, **keywordargs):
	context = {}	
	context['movie'] = request.POST.get('movie')
	movie_list = ["Queen", "Ek Tha Tiger", "Joker"]

	if context['movie'] not in movie_list:
		return render(request, 'movie_not_present.html', context)

	def get_review(input_sentence):
		tkens = input_sentence.split()
		if "not" in tkens:
			if tkens[tkens.index("not")+1] != "bad":
				return 0

		import spacy
		from spacy.lang.en.stop_words import STOP_WORDS
		nlp = spacy.load('en_core_web_sm')

		import pandas as pd
		from sklearn.feature_extraction.text import TfidfVectorizer
		from sklearn.svm import LinearSVC
		from sklearn.pipeline import Pipeline
		from sklearn.model_selection import train_test_split

		data_yelp = pd.read_csv('yelp_labelled.txt', sep='\t', header = None)
		columns_name = ['Review', 'Sentiment']
		data_yelp.columns = columns_name

		data_amazon = pd.read_csv('amazon_cells_labelled.txt', sep = '\t', header = None)
		data_amazon.columns = columns_name

		data_imdb = pd.read_csv('imdb_labelled.txt', sep = '\t', header = None)
		data_imdb.columns = columns_name

		data = data_yelp.append([data_amazon, data_imdb], ignore_index=True)
		data = data.dropna()
		
		def text_data_cleaning(sentence):
			return sentence.split()

		tfidf = TfidfVectorizer(tokenizer = text_data_cleaning)
		classifier = LinearSVC()

		X = data['Review']
		y = data['Sentiment']

		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
		
		pipe = Pipeline([('tfidf', tfidf), ('pipe', classifier)])
		pipe.fit(X_train, y_train)

		return int(pipe.predict([input_sentence])[0])

	mapping = {
		1: "Positive",
		0: "Negative"
	}
	
	# spell checker
	from textblob import TextBlob
	corrected_review = TextBlob(request.POST.get('review')).correct()

	# get unique id
	review = get_review(str(corrected_review))
	uniq_id = uuid.uuid1()
	
	# if review Sentiment is positive, add to positive
	if review == 1:
		x = Reviews(
			id=uniq_id.hex,
			name=request.POST.get('movie'),
			positive=1,
			negative=0
		)
		x.save()

	# if review is negative, add to negative
	if review == 0:
		x = Reviews(
			id=uniq_id.hex,
			name=request.POST.get('movie'),
			positive=0,
			negative=1
		)
		x.save()

	context['review_type'] = mapping[review]
	context['review'] = corrected_review
	
	return render(request, 'review_added.html', context)
	
def ratings_view(request, *args, **keywordargs):
	ratings = {}

	# queen ratings
	queen_pos = 0
	queen_neg = 0
	for i in Reviews.objects.raw('SELECT 1 as id, * FROM sentiment_analyser_reviews WHERE name=\'Queen\''):
		if i.positive == 1:
			queen_pos += 1
		if i.negative == 1:
			queen_neg += 1

	# ek tha tiger ratings
	tiger_pos = 0
	tiger_neg = 0
	for i in Reviews.objects.raw('SELECT 1 as id, * FROM sentiment_analyser_reviews WHERE name=\'Ek Tha Tiger\''):
		if i.positive == 1:
			tiger_pos += 1
		if i.negative == 1:
			tiger_neg += 1

	# joker ratings
	joker_pos = 0
	joker_neg = 0
	for i in Reviews.objects.raw('SELECT 1 as id, * FROM sentiment_analyser_reviews WHERE name=\'Joker\''):
		if i.positive == 1:
			joker_pos += 1
		if i.negative == 1:
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