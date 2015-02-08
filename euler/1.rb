sum = 0
for a in 1.upto(999)
	if a % 3 == 0 || a % 5 == 0
		sum += a
	end
end

print sum

