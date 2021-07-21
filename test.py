from javascript import console, Array

a = Array([1, 2, 3, 3])
b = a.flatMap(lambda x,i: [x+i])
console.log(b)