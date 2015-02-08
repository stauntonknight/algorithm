def printL(n)
  if n == 0
    return ""
  end
a=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred","aand","thousand"]
  if n < 20
    return a[n-1]
  end
  if n < 100
   s = n / 10
   x = n%10
   if x > 0
    return a[s+20-3] + a[x - 1] 
   else
     return a[s+20-3] + ""
   end
  end 
  if ( n < 1000)
    s = n / 100
    t = n%100
    x = printL(t)
    p x
    if x.length > 0
      x = "and#{x}"
    end
    p x
    p a[s-1] + x
    t = "#{a[s-1]}hundred#{x}"
    p t
    return t
  end
  return "onethousand"
end
ans= 0
1.upto(1000) do |t|
  ans += (printL t).length
end
p ans


