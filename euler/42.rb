line = File.read("/Users/agarwalvivek/Downloads/p042_words.txt")
puts line
words = line.split(",")
words.map! { |word|
    word.gsub!("\"","")
    word.gsub!("\"" "")
}
a = words.map { |word|
    puts word
    ans = 0
    for ch in word do
        puts ch
        ans = ans + ch.getbyte(0) - "a".getbyte(0) + 1
        puts ans
    end
}

