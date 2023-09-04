
def swap(arr,x,y):
    arr[x],arr[y]=arr[y],arr[x]
    

def pal(word, start, end):
    if start is end:
        print(' '.join(word))
        return
    for i in range(start,end+1):
        swap(word,start,i)
        pal(word, start+1, end)
        swap(word,start,i)

word=input("Enter your word: ")
word_list=list(word)
length=len(word_list)
pal(word_list,0,length-1)
