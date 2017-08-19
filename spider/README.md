# Leetcode 爬虫

## 支持异步和多线程

> 注意
>
> PS：异步还没做 >_<，无聊的时候会加上去
> PSS：由于初期不知道哪些需要爬取，为了避免重复请求 leetcode 网站，在题目并不多的情况下，将所有的网页都下载下来，进行爬取，目前是 500 个网页，50 多M左右。

运行多线程的函数都是复制粘贴的，稍有冗余，大概也是无聊的时候会改。

增加题目 problems 下各种语言的模版代码，数组形式：[{ },{ },]，比如：

[{'value': 'cpp', 'text': 'C++', 'defaultCode': 'class Solution {\u000D\u000Apublic:\u000D\u000A    string getHint(string secret, string guess) {\u000D\u000A        \u000D\u000A    }\u000D\u000A}\u003B' },{'value': 'java', 'text': 'Java', 'defaultCode': 'class Solution {\u000A    public String getHint(String secret, String guess) {\u000A        \u000A    }\u000A}' },{'value': 'python', 'text': 'Python', 'defaultCode': 'class Solution(object):\u000D\u000A    def getHint(self, secret, guess):\u000D\u000A        \u0022\u0022\u0022\u000D\u000A        :type secret: str\u000D\u000A        :type guess: str\u000D\u000A        :rtype: str\u000D\u000A        \u0022\u0022\u0022' },{'value': 'c', 'text': 'C', 'defaultCode': 'char* getHint(char* secret, char* guess) {\u000D\u000A    \u000D\u000A}' },{'value': 'csharp', 'text': 'C#', 'defaultCode': 'public class Solution {\u000D\u000A    public string GetHint(string secret, string guess) {\u000D\u000A        \u000D\u000A    }\u000D\u000A}' },{'value': 'javascript', 'text': 'JavaScript', 'defaultCode': '/**\u000D\u000A * @param {string} secret\u000D\u000A * @param {string} guess\u000D\u000A * @return {string}\u000D\u000A */\u000D\u000Avar getHint \u003D function(secret, guess) {\u000D\u000A    \u000D\u000A}\u003B' },{'value': 'ruby', 'text': 'Ruby', 'defaultCode': '# @param {String} secret\u000D\u000A# @param {String} guess\u000D\u000A# @return {String}\u000D\u000Adef get_hint(secret, guess)\u000D\u000A    \u000D\u000Aend' },{'value': 'swift', 'text': 'Swift', 'defaultCode': 'class Solution {\u000D\u000A    func getHint(_ secret: String, _ guess: String) \u002D\u003E String {\u000D\u000A        \u000D\u000A    }\u000D\u000A}' },{'value': 'golang', 'text': 'Go', 'defaultCode': 'func getHint(secret string, guess string) string {\u000A    \u000A}' },{'value': 'scala', 'text': 'Scala', 'defaultCode': 'object Solution {\u000A    def getHint(secret: String, guess: String): String \u003D {\u000A        \u000A    }\u000A}' },]