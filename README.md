# Product_Recommender_app

In this application, we take book as product.

## Popularity and collaborative filtering based book recommended system

This application is a recommender system built for book lovers. 

# Input Data:

* Books  
Features: [ISBN, Book-Title, Book-Author, Year-Of-Publication, Publisher, Image-URL-S, Image-URL-M, Image-URL-L]

* Users  
Feature: [User-ID, Location, Age]

* Ratings 
Fetures: [User-ID	ISBN	Book-Rating]

## What is Recommender System?

Recommender systems are defined as recommendation inputs given by the people, which the system then aggregates and directs to appropriate recipients.  It can be further defined as a system that produces individualized recommendations as output or has the effect of guiding the user in a personalized way to interesting objects in a larger space of possible options. 

There are majorly Four types of recommender systems:

1. Popularity based Recommender System
2. Content based Recommender System
3. Collabrative filtering based Recommender System
4. Hybrid Recommender System


In this Application, we are following popularity based and Collabrative filtering based Recommender System.


## Population based Recommender system:

Aim: our main aim is to find out based book with high ratings.

Condition : Mimnimum no. of ratings per book should be greater than 250


## Collabrative Filtering abased Recommender system:

Aim: our main aim is to find out based book with high similarity.

Condition: Select that user who give more than 200 rating from entire users and filter that book which have more than 50 rating.

Developed the application by using Flask Framework.

## Output

* Popular top 50 Books are showing on the home page.


![](Screenshot%202022-09-27%20005801.jpg)




* In Recommended section, If You serch any book then, similar books are showing.



![](Screenshot%202022-09-27%20011647.jpg)




* Here, We can see that top 5 recommended books are showing.




![](Screenshot%202022-09-27%20011714.jpg)
