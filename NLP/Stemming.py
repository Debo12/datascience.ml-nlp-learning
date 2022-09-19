import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""

sentences = nltk.sent_tokenize(paragraph)
stemmerObj = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmerObj.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)

# OUTPUT
# ['i three vision india .', 'in 3000 year histori , peopl world come invad us , captur land , conquer mind .', 'from alexand onward , greek , turk , mogul , portugues , british , french , dutch , came loot us , took .', 'yet done nation .', 'we conquer anyon .', 'we grab land , cultur , histori tri enforc way life .', 'whi ?', 'becaus respect freedom others.that first vision freedom .', 'i believ india got first vision 1857 , start war independ .', 'it freedom must protect nurtur build .', 'if free , one respect us .', 'my second vision india ’ develop .', 'for fifti year develop nation .', 'it time see develop nation .', 'we among top 5 nation world term gdp .', 'we 10 percent growth rate area .', 'our poverti level fall .', 'our achiev global recognis today .', 'yet lack self-confid see develop nation , self-reli self-assur .', 'isn ’ incorrect ?', 'i third vision .', 'india must stand world .', 'becaus i believ unless india stand world , one respect us .', 'onli strength respect strength .', 'we must strong militari power also econom power .', 'both must go hand-in-hand .', 'my good fortun work three great mind .', 'dr. vikram sarabhai dept .', 'space , professor satish dhawan , succeed dr. brahm prakash , father nuclear materi .', 'i lucki work three close consid great opportun life .', 'i see four mileston career']
