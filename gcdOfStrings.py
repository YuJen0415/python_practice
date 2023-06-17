str1 = "ABCABC"
str2 = "ABC"

if str1 + str2 != str2 + str1:
    return ""

return str1[:gcd(len(str1), len(str2))]

# find the greatest common divisor for the string length