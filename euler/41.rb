a = Array.new(100000000, false)
a[1] = true
a[2] = true
a[3] = true
for i in 2..10000
    j = i * i
    while j < 100000000
       j = j + i
       j++ 
