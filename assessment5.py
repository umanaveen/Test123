my_dis_list={ 'a': 5,'b': 2,'c': 3,}
print(f"Sum of Dictionary : ",sum(my_dis_list.values()))


myDict = {'uma': 10, 'devi': 9,'anu': 15, 'abi': 10,'navin': 2, 'kavi': 32}
 
# myKeys = list(myDict.keys())
# myKeys.sort()
myDicted =sorted(myDict.items())
# keys = list(sorted(myDict.keys()))
# values = list(sorted(myDict.values()))
print (myDicted)
count = 0
def frequencycheck(string,my_string):
    count = 0
    for value in my_string.values():
        if value == string:
            count+=1
    return count
my_string = {'apple': 'red', 'banana': "Yellow",'carrot': 'orange', 'cherry': 'red','redchili': "red", 'orange': "orange"}
checkstring='red'
Result= frequencycheck(checkstring,my_string)
print(f"The frequency of words", checkstring,Result)



string = 'Python is great and Java is also great'
# print(' '.join(set(string.split())))

mylist = ["a", "b", "a", "c", "c"]
setdist =set(string.split())
mylist_result = list(dict.fromkeys(setdist))
print(mylist_result)