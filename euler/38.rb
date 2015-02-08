a = []
1.upto(9) do |t|
    a.push(t)
end
nums = a.permutation.to_a.reverse

for i in 0..nums.length-1
    num = nums[i]
    num_s = num.join.to_s
    1.upto(5) do |num_dig|
        testnum = num[0..num_dig-1].join.to_i
        actual_s = ""
        1.upto(10) do |mul|
            actual_s = actual_s + (testnum * mul).to_s
            if (actual_s.size == 9 && actual_s == num_s)
                puts num_s
                exit
            end
            if actual_s.size > 9
                break
            end
        end
    end
end
