a = (0..9).to_a.permutation.to_a
a = a.map(&:join).map(&:to_i)

def checkNum(a)
    t = [17, 13,11,7,5,3,2]
    for x in t do
        if ((a % 1000) % x) != 0 then
            return false
        end
        a = a/10
    end
end
sum = 0
for x in a do
    if checkNum(x) then
        sum = sum + x
    end
end
puts sum
