with open("story.txt","r") as f:
    story=f.read()

list_of_words=set()
start_of_word=-1 #let us assume

for i,char in enumerate(story):
    if char=="<":
        start_of_word=i
    if char==">" and start_of_word!=-1:
        word= story[start_of_word : i+1]
        list_of_words.add(word)
        start_of_word=-1 #so resetting for further new word

print(list_of_words)
story_ans={}
for word in list_of_words:
    answer=input("enter a word for "+word+": ")
    story_ans[word]=answer

for word in list_of_words:
    story=story.replace(word,story_ans[word])
    #as it gives new string and we want to make change in original story so, 

print(story)