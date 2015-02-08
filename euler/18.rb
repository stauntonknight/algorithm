file = File.new('18.in', 'r')
nR = 0
pyr = []
while (line = file.gets) 
  nR += 1
  nums = line.split(" ").map { |item| 
            item.to_i
         }
  pyr << nums
end
file.close
max = Array.new(nR) { Array.new(nR) }
0.upto(nR-1) do |i|
  max[nR-1][i] = pyr[nR-1][i]
end
(nR - 2).downto(0) do  |i|
  0.upto(i) do |j| 
    max[i][j] = pyr[i][j] + (max[i+1][j] > max[i+1][j+1] ? max[i+1][j]:max[i+1][j+1])
  end 
end
p max[0][0]
