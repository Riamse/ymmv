import newspaper

fox_news = newspaper.build("http://cnn.com")

for index,article in enumerate(fox_news.articles):
    article.download()
    article.parse()
    with open("article.txt","a") as fh:
        fh.write(article.text)

#end
