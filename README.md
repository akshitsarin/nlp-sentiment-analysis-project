# nlp-sentiment-analysis-project

## CS: 491 - Natural Language Processing [Final Project]

![nlp-screenshot](https://user-images.githubusercontent.com/30521594/127209660-77aadceb-9487-4342-a6e5-411d5fe4eeee.png)

[**`Presentation Link`**](https://docs.google.com/presentation/d/15bnM_Julzz9BB9RG3rLGYdzpCSR8XyrgbjFsFnjaELk/edit?usp=sharing)
[**`Project Link`**](https://nlp-review-analyser.herokuapp.com) <br>

Created and deployed a **Sentiment Analyser**, to analyse and categorize incoming raw movie reviews as Positive / Negative. <br>
The WebApp on the backend updates the ratings of the said movie in **real-time**, based on the nature of the provided review. 

```
As a PoC (Proof of Concept), only 3 movies have been added to our movie-database:
  - Joker
  - Queen
  - Ek Tha Tiger
```

Dataset Used: [Sentiment Labelled Sentences DataSet](https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences)

## Process Pipeline:

- Input individual tokens per review
- Apply **TF-IDF Vectorization**, assuming each review from Amazon, Yelp, IMDb datasets to be an individual document
- Use a **Support Vector Classifier** for the classification process
- Repeat tuning of parameters until *desired accuracy* is achieved
