#Easy verison without functions 

def strip_punctuation(word):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in punctuation_chars:
        if char in word:
            word = word.replace(char,'')
    return word

with open('mycsv.csv','w') as file:
        #Columns
        file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score") 
        
        with open("positive_words.txt") as pos_file: #Storing postive words
            reader = pos_file.read().split("\n")
            pos_words = reader[35:len(reader)-1]  
            
        with open("negative_words.txt") as neg_file: #Storing negative words
            reader = neg_file.read().split("\n")
            neg_words = reader[35:len(reader)-1]
         
        with open("project_twitter_data.csv",'r') as tweet_file:
            for line_index, line in enumerate(tweet_file):
                if line_index == 0:
                    continue
                words = line.split(',')
                tweet = words[0].split()
                retweets, replies = words[1].strip(), words[2].strip()
                pos_score, neg_score = 0, 0
                for tweet_words in tweet:
                    tweet_words = strip_punctuation(tweet_words).lower()
                    if tweet_words in pos_words:
                        pos_score += 1
                    elif tweet_words in neg_words:
                        neg_score += 1
                file.write("\n {}, {}, {}, {}, {}".format(retweets, replies, pos_score, neg_score, pos_score-neg_score))
      