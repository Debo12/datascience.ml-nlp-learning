import nltk
from nltk.stem import WordNetLemmatizer
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
lemmatzerObj = WordNetLemmatizer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatzerObj.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)

print(sentences)

# OUTPUT
# ['I three vision India .', 'In 3000 year history , people world come invaded u , captured land , conquered mind .', 'From Alexander onwards , Greeks , Turks , Moguls , Portuguese , British , French , Dutch , came looted u , took .', 'Yet done nation .', 'We conquered anyone .', 'We grabbed land , culture , history tried enforce way life .', 'Why ?', 'Because respect freedom others.That first vision freedom .', 'I believe India got first vision 1857 , started War Independence .', 'It freedom must protect nurture build .', 'If free , one respect u .', 'My second vision India ’ development .', 'For fifty year developing nation .', 'It time see developed nation .', 'We among top 5 nation world term GDP .', 'We 10 percent growth rate area .', 'Our poverty level falling .', 'Our achievement globally recognised today .', 'Yet lack self-confidence see developed nation , self-reliant self-assured .', 'Isn ’ incorrect ?', 'I third vision .', 'India must stand world .', 'Because I believe unless India stand world , one respect u .', 'Only strength respect strength .', 'We must strong military power also economic power .', 'Both must go hand-in-hand .', 'My good fortune worked three great mind .', 'Dr. Vikram Sarabhai Dept .', 'space , Professor Satish Dhawan , succeeded Dr. Brahm Prakash , father nuclear material .', 'I lucky worked three closely consider great opportunity life .', 'I see four milestone career']