"""编辑距离是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。通常来说，编辑距离越小，两个文本的相似性越大。这里的编辑操作主要包括三种：

插入：将一个字符插入某个字符串；
删除：将字符串中的某个字符删除；
替换：将字符串中的某个字符替换为另外一个字符。
那么，如何用Python计算编辑距离呢？我们可以从较为简单的情况进行分析。

当两个字符串都为空串，那么编辑距离为0；
当其中一个字符串为空串时，那么编辑距离为另一个非空字符串的长度；
当两个字符串均为非空时(长度分别为 i 和 j )，取以下三种情况最小值即可：
1、长度分别为 i-1 和 j 的字符串的编辑距离已知，那么加1即可；
2、长度分别为 i 和 j-1 的字符串的编辑距离已知，那么加1即可；
3、长度分别为 i-1 和 j-1 的字符串的编辑距离已知，此时考虑两种情况，若第i个字符和第j个字符不同，那么加1即可；如果相同，那么不需要加1。
很明显，上述算法的思想即为动态规划。

求长度为m和n的字符串的编辑距离，首先定义函数——edit(i, j)，它表示第一个长度为i的字符串与第二个长度为j的字符串之间的编辑距离。动态规划表达式可以写为：

if i == 0 且 j == 0，edit(i, j) = 0
if （i == 0 且 j > 0 ）或者 （i > 0 且j == 0），edit(i, j) = i + j
if i ≥ 1 且 j ≥ 1 ，edit(i, j) == min{ edit(i-1, j) + 1, edit(i, j-1) + 1, edit(i-1, j-1) + d(i, j) }，当第一个字符串的第i个字符不等于第二个字符串的第j个字符时，d(i, j) = 1；否则，d(i, j) = 0。
"""
def edit_distance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = np.zeros((len1 + 1,len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i    
    for j in range(len2 + 1):
        dp[0][j] = j
     
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            delta = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i - 1][j - 1] + delta, min(dp[i-1][j] + 1, dp[i][j - 1] + 1))
    return dp[len1][len2]
