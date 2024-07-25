import tkinter as tk #graphical interface
import nltk #NLP
from textblob import TextBlob #sentiments
from newspaper import Article #fornewspaper



def func():
    url=utext.get('1.0', "end").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    

    text=article.text
    news=TextBlob(article.summary)
    senti=news.polarity

    percentage=senti*100
    perc = round(percentage, 2)  
  
  
    title.config(state='normal')
    author.config(state='normal')
    date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0','end')
    title.insert('1.0',article.title)

    author.delete('1.0','end')
    author.insert('1.0',article.authors)

    date.delete('1.0','end')
    date.insert('1.0',article.publish_date)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    
    sentiment.delete('1.0','end')
    
    if(senti<0):
      sentiment.insert('1.0',f'Article is on a negative side , Negativity: {perc}%')
    elif(senti>0):
      sentiment.insert('1.0',f'Article is on a positive side , Positivity: {perc}%')
    else:
      sentiment.insert('1.0',f'Article seems Neutral')


    title.config(state='disabled')
    author.config(state='disabled')
    date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='dissbled')
    
   
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1920x1080')

tlabel=tk.Label(root,text="Title")
tlabel.pack()
title=tk.Text(root,height=2,width=140)
title.config(state='disabled',bg='#98AFC7')
title.pack()

alabel=tk.Label(root,text="Authors")
alabel.pack()
author=tk.Text(root,height=1,width=140)
author.config(state='disabled',bg='#98AFC7')
author.pack()

dlabel=tk.Label(root,text="Published On:")
dlabel.pack()
date=tk.Text(root,height=1,width=140)
date.config(state='disabled',bg='#98AFC7')
date.pack()

slabel=tk.Label(root,text="Summary")
slabel.pack()
summary=tk.Text(root,height=22,width=140)
summary.config(state='disabled',bg='#98AFC7')
summary.pack()


stlabel=tk.Label(root,text="Sentiments")
stlabel.pack()
sentiment=tk.Text(root,height=1,width=140)
sentiment.config(state='disabled',bg='#98AFC7')
sentiment.pack()

ulabel=tk.Label(root,text="Enter Article URL")
ulabel.pack()
utext=tk.Text(root,height=1,width=140)
utext.config(bg='#FBE7A1')
utext.pack()

btnlabel=tk.Label(root,text=" ")
btnlabel.pack()
btn=tk.Button(root, text="Summarize",command=func)
btn.pack()

root.mainloop()
