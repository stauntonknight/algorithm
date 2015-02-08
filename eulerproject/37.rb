require 'mathn'
$a = [1,2,3,5,7,9]
$count = 0
$sum = 0

def check_prime(num) 
	num_s = num.to_s
	is_found = 1
	0.upto(num_s.length - 1) do |i|
		substr = num_s[0..i]
		if !substr.to_i.prime?
			is_found = 0
			break
		end
	end
	0.upto(num_s.length - 1) do |i|
		substr = num_s[i..num_s.length - 1]
		if !substr.to_i.prime?
			is_found = 0
			break
		end
	end
	if is_found == 1
		$count = $count + 1
		$sum = $sum + num
	end 
end

def getNum(dig, num)
	if $count == 11
		return
	end
	if dig == 0
		check_prime(num)
		return
	end
	if $count == 11
		return
	end
	for i in $a
		getNum(dig - 1, num * 10 + i)
	end
end

num_dig = 2
while true
	getNum(num_dig, 0)
	if $count == 11
		print $sum
		print "\n"
		break
	end
	num_dig = num_dig + 1
end

