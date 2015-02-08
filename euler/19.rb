months = [31,28,31,30,31,30,31,31,30,31,30,31]
start = 2
count = 0
1901.upto(2000) do |year|
  leap = (year % 400 == 0 ) || (year % 4 == 0 && year % 100 != 0)
  ind = 0
  months.each do |day|
    start = start % 7
    p "#{year} -> #{ind} -> #{start}"
    if start == 0
      count = count + 1 
    end
    
    if ind == 1 && leap
      day = day + 1   
    end
    start = start + day 
    ind = ind + 1
  end
end

print count
