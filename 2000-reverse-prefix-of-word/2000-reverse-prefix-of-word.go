func reversePrefix(word string, ch byte) string {
    var ans string

    for i := 0; i < len(word); i++ {
        if (word[i] == ch) {
            ans = word[i + 1: ]
            for j := 0; j < i + 1; j++ {
                ans = string(word[j]) + ans
            }
            return ans
        }
    }
    return word
}