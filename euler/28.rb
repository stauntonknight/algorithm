def getSumCorners(n) 
  return 1 if n == 1
  sum = n*n + n*n - n + 1 + n*n - 2*n + 2 + n*n - 3*n + 3
  return sum
end
sum = 0
(1..1001).step(2) do |i|
  sum += getSumCorners(i)
end
p sum
