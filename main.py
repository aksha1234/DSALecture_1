## So here I will be making the dsa algorithm
## What I called as the binary search and linear search program 
def locate_card(cards,query):
  pass

## Now just I will be making the filter
cards=[1,2,3,4,5,7,8,9]
query=4
output=3
result=locate_card(cards,query)
print(result)
print(result==output)

tests={'input':{'cards':[5,7,8,9,10],'query':[10]},'output':[4]}

locate_card(**tests['input'],)
