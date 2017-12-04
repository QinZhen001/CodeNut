/**
 * Created by qinzhen on 2017/9/3.
 */
export const slides = [
  {
    linkProblemId: '8B9',
    picUrl: 'static/slides/slide_1.png'
  },
  {
    linkProblemId: 'oX4',
    picUrl: 'static/slides/slide_2.png'
  },
  {
    linkProblemId: 'jMK',
    picUrl: 'static/slides/slide_3.png'
  },
  {
    linkProblemId: 'KeK',
    picUrl: 'static/slides/slide_4.png'
  },
  {
    linkProblemId: 'jL9',
    picUrl: 'static/slides/slide_5.png'
  }
]

export const hotKeys = ['Array', 'Search', 'Tree', 'String',
  'Backtracking', 'Math', 'Dynamic Programming', 'Hash']

export const editorThemes = ['default', 'base16-dark', 'ambiance',
  'paraiso-light', 'cobalt', 'paraiso-dark', 'rubyblue', 'mbo', 'solarized']

export const keyMaps = ['sublime', 'emacs', 'vim']

export const editorModes = ['text/x-csrc', 'text/x-c++src', 'text/x-csharp', 'text/x-java', 'text/x-python', 'text/javascript', 'text/x-ruby', 'text/x-go']

export const languages = ['C', 'C++', 'C#', 'Java', 'Python3', 'JavaScript', 'Ruby', 'Go']

export const templets = [
  {value: 'c', text: 'C', defaultCode: ''},
  {value: 'cpp', text: 'C++', defaultCode: ''},
  {value: 'csharp', text: 'C#', defaultCode: ''},
  {value: 'java', text: 'Java', defaultCode: ''},
  {value: 'python3', text: 'Python3', defaultCode: ''},
  {value: 'javascript', text: 'Javascript', defaultCode: ''},
  {value: 'ruby', text: 'Ruby', defaultCode: ''},
  {value: 'golang', text: 'Go', defaultCode: ''}
]

export const templateCodes = [
  {text: 'C', defaultCode: 'int findMaximumXOR(int* nums, int numsSize) {\n\n}'},
  {text: 'C++', defaultCode: 'class Solution {\npublic:\n     int findMaximumXOR(vector<int>& nums) {\n\n     }\n};'},
  {text: 'C#', defaultCode: 'class Solution {\n    public int findMaximumXOR(int[] nums) {\n\n    }\n}'},
  {
    text: 'Java',
    defaultCode: 'class Solution {\n\n}'
  },
  {
    text: 'Python3',
    defaultCode: 'class Solution(object):\n    def findMaximumXOR(self, nums):\n      """\n      :type nums: List[int]\n      :rtype: int\n      """'
  },
  {text: 'javascript', defaultCode: 'function(s) {\n\n};'},
  {text: 'Ruby', defaultCode: 'class Solution {\n    func findMaximumXOR(_ nums: [Int]) -> Int {\n\n    }\n}'},
  {text: 'Go', defaultCode: 'func findMaximumXOR(nums []int) int {\n\n}'}
  // 'class Solution {\n    func findMaximumXOR(_ nums: [Int]) -> Int {\n\n    }\n}',
  // 'func findMaximumXOR(nums []int) int {\n\n}'
]

export const selfStudyItems = [
  {
    title: '使用位运算交换两个数',
    description: '算法解析A是位异或的运算符，即比较相同两位的异同，如果相同，则赋值为0，否则为1。在本程序中a、b的初始值分别为3和5，对应的二进制分别为00000011和00000101。经过下面的3个步骤..',
    difficulty: 1.5,
    attention: 3596
  },
  {
    title: '最接近数的完整程序源码',
    description: '问题设计算法求数组中相差最小的两个元素（称为最接近数）的差。要求分别给出伪代码和C++描述。程序源码完整的程序源代码如下：//采用分治法//对数组先进行快速排序//在依次比较..',
    difficulty: 2.0,
    attention: 1254
  },
  {
    title: '众数的完整程序源代码',
    description: '问题在一个序列中出现次数最多的元素称为众数。程序源码完整的程序源代码如下：//先对序列进行快速排序//再进行一次遍历//输出众数的重复次数#include "iostream"usingnamesp..',
    difficulty: 3.6,
    attention: 3642
  },
  {
    title: '完美数的完整程序源码',
    description: '一、问题圣经上说：神6天创造天地万有，第7日安歇。为什么是6天呢？任何一个自然数的因数中都有1和它本身，所有小于它本身的因数称为这个数的真因数，如果一个自然数的真因数之和..',
    difficulty: 4.1,
    attention: 9513
  },
  {
    title: '数组中的最大元素（分治法）',
    description: '问题设计分治算法求一个数组中的最大元素。算法分析简单的分治问题将数组均衡的分为“前”，“后”两部分分别求出这两部分最大值，然后再比较这两个最大值程序源码完整的程序源代..',
    difficulty: 1.7,
    attention: 3459
  },
  {
    title: '货币兑付问题的完整程序源码',
    description: '问题考虑下面的货币兑付问题：在面值为(v1, v2, …, vn)的n种货币中，需要支付y值的货币，应如何支付才能使货币支付的张数最少，即满足，且使最小（xi是非负整数）。设计动态规划算..',
    difficulty: 2.5,
    attention: 1456
  },
  {
    title: '求格雷码的完整程序源代码',
    description: '一、问题格雷码是一个长度为2n的序列，序列中无相同元素，且每个元素都是长度为n的二进制位串，相邻元素恰好只有1位不同。例如长度为23的格雷码为(000, 001, 011, 010, 110, 111..',
    difficulty: 3.4,
    attention: 1485
  },
  {
    title: '矩阵乘法的程序源码（完整源码）',
    description: '一、 矩阵乘法矩阵的乘法要相对复杂些。对于给定的m×n矩阵A和n×k矩阵B,其乘积矩阵为：C=AB这里，乘积矩阵C为m×k阶的。两个矩阵参与相乘的前提条件是，矩阵A的列数必须等于矩阵B的..',
    difficulty: 1.8,
    attention: 7531
  },
  {
    title: '兔子产仔问题的程序源代码（完整源码）',
    description: '一、兔子产仔兔子产仔是一个非常古老而经典的问题，其与数论有关。兔子产仔问题最早记载于13世纪意大利数学家斐波那契的《算盘书》，其大意如下：如果一对两个月大的兔子以后每..',
    difficulty: 1.6,
    attention: 9513
  },
  {
    title: '产生任意范围的随机数',
    description: '一、 产生任意范围的随机数例如，需要一个[m,n]之间的浮点随机数，则可以采用如下方法获得：下面给出完整的程序代码，示例如下：该程序的基本结构和《[0, 1]之间均匀分布的随机数..',
    difficulty: 2.4,
    attention: 6435
  },
  {
    title: '爱因斯坦的阶梯问题的程序源代码（完整源码）',
    description: '一、爱因斯坦的阶梯爱因斯坦的阶梯问题是一个有趣的数论问题，爱因斯坦的阶梯大意如下：有一天爱因斯坦给他的朋友出了一个题目，有一个楼，其两层之间有一个很长的阶梯。如果一个..',
    difficulty: 3.9,
    attention: 1549
  },
  {
    title: '洗扑克牌算法的实现源代码（完整程序）',
    description: '扑克牌是一种非常大众化的游戏，在计算机中有很多与扑克牌有关的游戏。例如，在Windows操作系统下自带的纸牌、红心大战等。在扑克牌类的游戏中，往往都需要执行洗牌操作，就是将一..',
    difficulty: 4.2,
    attention: 7469
  },
  {
    title: '[m,n]之间均匀分布的随机整数算法的实现源码（完整程序）',
    description: '一、 [m,n]之间均匀分布的随机整数算法了解了[0，1]之间均匀分布的随机数算法，若需要得到随机的整数，则会比较容易。只需将结果取整即可。例如，若需要得到[m,n]之间均匀分布的随..',
    difficulty: 5.0,
    attention: 2635
  },
  {
    title: '生命游戏算法的实现源码（完整程序）',
    description: '生命游戏又称为细胞自动机游戏，或者元胞自动机游戏。生命游戏是英国数学家J.H.Conway首次提出的。在1970年，J.H.Conway小组正在研究一种细胞自动装置，J.H.Conway从中获得启发，..',
    difficulty: 1.2,
    attention: 5689
  },
  {
    title: '—次一密加密、解密算法的源代码（完整程序）',
    description: '经典的密码体系不能够严格保证安全，简单地说，其大都依靠复杂的算法使得破译比较困难。但是随着计算机技术的飞速发展，一些看似不可破译的算法正在被逐个攻破。例如，在1977年，..',
    difficulty: 1.6,
    attention: 5614
  },
  {
    title: '怎样实现金额转换问题的程序源码',
    description: '一、怎样实现金额转换金额转换，阿拉伯数字的金额转换成汉字大写的形式如下。(YI011)à(壹仟零壹拾壹元整)输出。算法分析金额转换，在开发财务相关软件时会经常用到，也是软件本地..',
    difficulty: 2.3,
    attention: 7391
  },
  {
    title: '天平称物问题的程序源码',
    description: '一、天平称物有4个砝码，总重量为40克，砝码的重量是整数，且各不相等。请确定它们的重量，使之能称出1〜40克之间任何整数重量的物体。算法分析(1) 一个砝码重量生成器。生成4个砝码..',
    difficulty: 3.1,
    attention: 4316
  },
  {
    title: '双色球随机摇号问题的程序源码',
    description: '一、双色球随机摇号用计算机模拟双色球摇号，根据福利彩票双色球玩法规则，6个蓝色球，数字范围1~32,不允许重复，1个红色球，范围1~16,用计算机自动生成6个蓝色球，1个红色球。算法..',
    difficulty: 3.7,
    attention: 5689
  },
  {
    title: '数字组合问题的程序源码',
    description: '一、数字组合将丨、2、3、4、5、6、7、8、9这9个数字分成三个百位数.每个数字用且只用一次，并且第三个数是第一个数的3倍，第二个数是第一个数的两倍。求三个数。说明，结果可能多于一组，..',
    difficulty: 1.1,
    attention: 4719
  },
  {
    title: '数字拆解问题的程序源码',
    description: '一、数字拆解将任一个数字进行拆解，最大数不超过2,例如。3=2+1=1+2=1+1+1,共3种拆法。4=3+1=2+2=2+1+1=1+2+1=1+1+1+1,共5种拆法。5=2+2+1=2+1+2=2+1+1+1=1+2+2=1+2+1+1=1+1+2+1..',
    difficulty: 2.2,
    attention: 1653
  },
  {
    title: '图的深度优先遍历（邻接表存储）',
    description: '一、问题选择从淮安出发，然后青岛、烟台、大连、西安、开封、上海、苏州和扬州旅游路线，每一条路线尽量延伸到所有城市。算法分析①假设图G的初始状态是所有顶点均未曾访问过，在G中任..',
    difficulty: 3.4,
    attention: 5689
  },
  {
    title: '图的概述及建立（邻接矩阵存储）',
    description: '一、图的概念及相关术语1、图的概念1）、图的定义：记为G=(V，E)，其中V是顶点的有穷非空集合，E是边的有穷集合。2）、无向图的定义：每条边都是没有方向的图。3）、有向图的定义：每条边都..',
    difficulty: 3.1,
    attention: 9745
  },
  {
    title: '二叉树中序遍历（孩子链表示法）',
    description: '一、树形结构实例描述树形结构是一类重要的非线性结构。树形结构是结点之间有分支，并具有层次关系的结构。 二、树的定义树是n(n≥0)个结点的有限集T。结点..',
    difficulty: 2.5,
    attention: 8513
  },
  {
    title: '队列常用操作（链式队列）',
    description: '一、队列的定义队列是只允许在一端进行插入，而在另一端进行删除的运算受限的线性表。操作原则：先进先出或者后进后出。 二、队列的基本运算1、InitQueue(Q..',
    difficulty: 1.3,
    attention: 9342
  },
  {
    title: '应用栈实现进制转换',
    description: '问题实现应用栈实现进制的转换，可以将十进制数转换为其他进制数。算法分析栈具有后进先出的固有特性，使栈称为了程序设计中有用的工具。这里实现的是十进制数n和其他进制数d的..',
    difficulty: 3.7,
    attention: 6451
  },
  {
    title: '使用头插入法建立单链表',
    description: '问题实现使用头插入法建立一个单链表，并将单链表输出在窗体上。算法分析头插入法创建单链表的算法思想是：先创建一个空表，生成一个新节点，将新节点插入到当前链表的表头节点..',
    difficulty: 4.6,
    attention: 5522
  },
  {
    title: '合并两个链表的完整程序源代码',
    description: '问题实现将两个链表合并，合并后的链表为原来两个链表的连接，即将第二个链表直接连接到第一个链表的尾部，合成为一个链表。算法分析主要思想是先找到熬第一个链表的尾节点，使..',
    difficulty: 1.2,
    attention: 4321
  },
  {
    title: '单链表节点逆置的完整程序源码',
    description: '问题创建一个单链表，并将链表中的节点逆置，将逆置后的链表输出在窗体上。算法分析主要思想：将单链表的节点按照从前往后的顺序依次取出，并依次插入到头节点的位置。程序源码完..',
    difficulty: 1.5,
    attention: 1447
  },
  {
    title: '平分七筐鱼问题的完整程序源码',
    description: '问题甲、乙、丙三位鱼夫出海打鱼，他们随船带了21只箩筐。当晚返航时，他们发现有七筐装满了鱼，还有七筐装了半筐鱼，另外七筐则是空的，由于他们没有秤，只好通过目测认为七个满筐..',
    difficulty: 1.9,
    attention: 1212
  },
  {
    title: '括号匹配检测（链表）的完整程序源码',
    description: '问题本实例要求编写检测括号是否匹配的程序，其主要功能是对输入的一组字符串进行检测，当输入的字符串括号（包括“｛｝”、“[]”、”()“）匹配时输出matching，否则输出no matching。算..',
    difficulty: 3.9,
    attention: 3737
  },
  {
    title: '马克思手稿中的数学题',
    description: '问题马克思手稿中有一道趣味数学问题：有30个人，其中有男人、女人和小孩，在一家饭馆吃饭花了50先令；每个男人花3先令，每个女人花2先令，每个小孩花1先令；问男人、女人和小孩各有..',
    difficulty: 3.7,
    attention: 7432
  },
  {
    title: '获取格林尼治平时的完整程序源码',
    description: '一、说明以本初子午线的平子夜算起的平太阳时，又称格林尼治平时或格林尼治时间。算法分析程序源码完整的程序源代码如下：#include "stdio.h"#include"time.h"voidmain(){struc..',
    difficulty: 2.9,
    attention: 6139
  },
  {
    title: '婚礼上的谎言问题的完整程序源代码',
    description: '问题3对情侣参加婚礼，3个新郎为A、B、C，3个新郎为X、Y、Z，有人想知道究竟谁是谁结婚，于是就问新人中的三位，得到结果：A说他将和X结婚；X说她的未婚夫是C；C说他将和Z结婚。这个人事..',
    difficulty: 1.6,
    attention: 4518
  },
  {
    title: '黑纸与白纸问题的完整程序源码',
    description: '问题5人对坐，每人都可以看到其它人额头上的纸的颜色。5 人相互观察后， A说：“我看见有3 人额头上贴的是白纸，1 人额头上贴的是黑纸。” B说：“我看见其它4人额头上贴的都是黑纸。”..',
    difficulty: 2.1,
    attention: 3419
  },
  {
    title: '塔灯数量问题的完整程序源码',
    description: '一、说明有一八层灯塔，每层的灯数都是上一层的2倍，共有765盏等，编程球最上层与最下层的灯数。二、分析程序源码完整的程序源代码如下：#include "stdio.h"intmain(){intn=1,m,su..',
    difficulty: 3.6,
    attention: 5285
  },
  {
    title: '老鼠走迷宫的完整程序源代码（C语言版）',
    description: '一、说明老鼠走迷宫是递回求解的基本题型，我们在二维阵列中使用2表示迷宫墙壁，使用1来表示老鼠的行走路径，试以程式求出由入口至出口的路径。二、解法老鼠的走法有上、左、下、右..',
    difficulty: 1.7,
    attention: 9634
  }
]

export const results = [
  {name: 'System Error', value: '设置错误或其他问题'},
  {name: 'Accepted', value: '成功运行并得到了正确的结果'},
  {name: 'Wrong Answer', value: '成功运行但到得了错误的结果'},
  {name: 'Dangerous System Call', value: '程序因为危险的系统调用被终止'},
  {name: 'Runtime Error', value: '程序因为类似于堆栈溢出的错误而被系统终止，即运行错误'},
  {name: 'Compile Error', value: '源代码无法被正确编译'},
  {name: 'Time Limit Exceed', value: '超过时间限制'},
  {name: 'Output Limit Exceed', value: '程序输出长度超过答案长度'},
  {name: 'Memory Limit Exceed', value: '超过内存限制'},
  {name: 'Run Successfully', value: '运行成功但是不可预知的错误发生'}
]

export const baseUrl = 'https://api.txdna.cn'

// export const baseUrl = '0.0.0.0:5000'
export const MSG_OK = 'ok'
export const MSG_NO = 'no'

