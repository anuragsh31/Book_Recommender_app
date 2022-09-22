import re
from flask import Flask,render_template, request
import pickle
import numpy as np
popularity_df=pickle.load(open('popular.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
similarity_score=pickle.load(open('similar.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def index():
    return render_template ('index.html',book_name=list(popularity_df['Book-Title'].values), 
                                        author=list(popularity_df['Book-Author'].values),
                                        image=list(popularity_df['Image-URL-M'].values),
                                        votes=list(popularity_df['num_ratings'].values),
                                        rating=list(popularity_df['avg_ratings'].values))

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input=request.form.get('user_input')
    index=np.where(pt.index==user_input)[0][0] # get the index of the perticular book title
    similar_item=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1], reverse=True)[1:6] # it's sort the similarity score
    data=[]
    for i in similar_item:
        item=[]
        #print(pt.index[i[0]])
        #suggetion=books[books['Book-Title'] == pt.index[i[0]]]# there are multiple book which title is same but different ISBN. so we drop the duplicate 
        temp=books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    
    print(data)
    return render_template('recommend.html',data=data)

if __name__=='__main__':
    app.run(debug=True)