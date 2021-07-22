from javascript import *
console.clear(0)

array = Array('apple', 'orange', 'cherry')
index = Math.floor(Math.random()*array.length)
console.info('Random element:',array[index])
console.table(array)