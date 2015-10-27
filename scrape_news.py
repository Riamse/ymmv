from __future__ import print_function
import newspaper

websites = 'http://mitadmissions.org', 
for url in websites:
    print("trying to scrape", url)
    site = newspaper.build(url)
    print("scraping", url)

    for index,article in enumerate(site.articles):
        article.download()
        article.parse()

        with open("article.txt","a") as fh:
            fh.write(article.text.encode("latin1", "ignore"))
        print("article", index, "is now processed")

#end
