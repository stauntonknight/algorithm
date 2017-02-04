primes = Array.new(1000001, true)
primes [2] = true
primes[3] = true
i = 2;
while i * i <= 1000000 do
    j = i*i
    while j < 1000000 do
       primes [j] = false 
       j = j + i
    end
    while primes[i] == false do
        i = i + 1
        if i > 1000000 then
            break
        end
    end
    if i  > 1000000 then
        break
    end
end
