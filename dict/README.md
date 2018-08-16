
## Dict Notes

Simply an unordered list of "key, value" pairs

Dictionary keys are always unique and must be of an immutable data type 
(strings, numbers, tuples)

Usually computationally faster than using lists, because often you may have
a list that you don't know the size of ahead of time, or at what index an elemtnt
exists


Function dict() requires a list of tuples as an argument


When would I use a dictionary instead of a list?
 - If you onlt care about data "existing", use a list
 - If you need to quickly access data to re-use it or modify it, use a dictionary"""

mydict = [{"one": "fish", "two": "fish", "red": "fish", "blue": "fish"}]
