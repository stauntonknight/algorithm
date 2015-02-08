BEGIN {
  tsum=0
  for (i=65;i<=91;i++)
    map[sprintf("%c", i)] = i
}
{
  split($0, chars, "")
  sum=0
  for(i=1;i<=length(chars);i++) {
    if ( chars[i] >= "A" && chars[i] <="Z")
      sum = sum + map[chars[i]] + 1 - map["A"]
  }
  sum = sum * NR
  tsum = tsum + sum
}
END {
  print tsum
}
