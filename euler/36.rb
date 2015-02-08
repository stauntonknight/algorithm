sum = 0;
0.upto(1) do |odd|
	1.step(10) do |numBits|
		n = (1 << numBits)
		n = n - 1
		1.step(n, 2) do |i|
			k = i
			t = 0
			count = 0
			while k!= 0
				t = t | (k&1)
				k = k >> 1
				count = count + 1
				if k > 0
					t = t << 1
				end
			end
			if odd > 0
				t = t << 1
			end
			0.upto(odd) do |num|
				if (odd > 0) 
					t = t | num
				end
				t = t << (2 * (numBits - count))
				num = t << count 
				num = num | i
				num_s = num.to_s
				if num_s == num_s.reverse
					if num < 1000000
						sum = sum + num
					end
				end
			end
		end
	end
end
print sum

