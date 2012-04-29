file = File.new("11.txt","r")
a = []
while(line = file.gets)
	array = []
 	line.split(" ").each {|num|
		if num.length > 0 
			array.push num.to_i
		end
	}
	a.push array
end
max = -1
r = a.length
c = a[0].length
0.upto(r-1) do |i|
  0.upto(c-1) do |j|
    if i +3 < r 
      now = a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
      max = now if now > max
    end
    if j + 3 < c 
      now = a[i][j] * a[i][j+1]*a[i][j+2]*a[i][j+3]
      max = now if now > max
    end
    dx = [1,-1]
    for curr in dx 
      if i + curr * 3 < 0 || i + curr * 3 >= r || j +3 >= c
        next
      end
      xs = i
      ys = j
      now = 1
      0.upto(3) do
        now = now * a[xs][ys]
        xs += curr
        ys += 1
      end
      max = now if now > max
    end
  end
end
p max
