require "prime"
a =  (1001..9999).to_a
a = a.select { |x| Prime.prime?(x) }
puts a.size
i = 0
while i < a.size
    j = i + 1
    while j < a.size
        t = false
        x = a[j] + a[j] - a[i]
        s1 = a[i].to_s.chars.sort.join
        s2 = a[j] .to_s.chars.sort.join
        s3 = x.to_s.chars.sort.join
        if s1 == s2 and s2 == s3 and Prime.prime?(x) then
            puts a[i]
            puts a[j]
            puts x
        end
        j = j + 1
    end
    i = i + 1
end
