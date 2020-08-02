def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char,'')
    return word.rstrip()

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

           
def get_pos(sentence): #storing positive words
    sentence = strip_punctuation(sentence)
    words = sentence.split()
    count = 0
    for word in words:
        if word in positive_words:
               count += 1
    return count
            
negative_words = []
with open("negative_words.txt") as pos_f: #storing negative words
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip()) 
            
def get_neg(sentence):
    sentence = strip_punctuation(sentence)
    words = sentence.split()
    count = 0
    for word in words:
        if word in negative_words:
                count += 1
    return count


with open('resulting_data.csv','w') as file:
        #Columns
        file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score") 
        file.write("\n")
        
        with open("project_twitter_data.csv",'r') as tweet_file:
            for line_index, line in enumerate(tweet_file):
                if line_index == 0:
                    continue
                words = line.strip().split(',')
                tweet = words[0]
                retweets, replies = words[1], words[2]
                pos_score, neg_score = get_pos(words[0]),get_neg(words[0])
                file.write("{}, {}, {}, {}, {}".format(retweets, replies, pos_score, neg_score, pos_score-neg_score))
                file.write("\n")