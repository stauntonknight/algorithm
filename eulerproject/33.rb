nn = 1
dd = 1
10.upto(99) do |i|
  j=i+1
  while j < 100
    num = i
    den = j
    j+=1
    num_s = num.to_s
    den_s = den.to_s
    is = false
    if (num_s[0] == den_s[0]) && (num_s[1].to_i * den == den_s[1].to_i * num)
      is = true
    end
    if (num_s[1] == den_s[1]) && (num_s[0].to_i * den == den_s[0].to_i * num)
      is = true
    end
    if (num_s[0] == den_s[1]) && (num_s[1].to_i * den == den_s[0].to_i * num)
      is = true
    end

    if (num_s[1] == den_s[0]) && (num_s[0].to_i * den == den_s[1].to_i * num)
      is = true
    end
    if num_s[0] == "0" || num_s[1] == "0" 
      is = false
    end
    p "#{num}/#{den}" if is
    nn *= num if is
    dd *= num if is
  end
end

d = nn.gcd(dd)
p dd/d

