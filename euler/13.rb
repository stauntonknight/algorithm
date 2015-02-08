file=File.new("13.txt","r")
a = 0
while ( line = file.gets)
  a = a + line.to_i
end
p a

