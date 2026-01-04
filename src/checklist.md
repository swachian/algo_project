|#   | Problem Name                                 | Category                    | Round 2 | Round 3     |  Round 4    |
|-----|----------------------------------------------|-----------------------------|------|------|------|
| 1   | Pair Sum - Sorted                            | Two Pointers                | ✅     |      | 2'     |
| 2   | Triplet Sum                                  | Two Pointers                | POK 12.08     | 20'     |   12'   |
| 3   | Valid Palindrome                             | Two Pointers                | ✅     |      |  5'    |
| 4   | Container With Most Water                    | Two Pointers                | ✅     |      | 4'     |
| 5   | Shift Zeroes                                  | Two Pointers                | NOK 12.09     |  5'    |   2'   |
| 6   | Next Lexicographical Sequence                | Two Pointers                | ✅ 稍欠火候      |      |   20' 还是有点忘了   |
| 7   | Pair Sum - Unsorted                          | Hash Map & Set              | ✅      |      |   1'   |
| 8   | Valid Sudoku                                 | Hash Map & Set              | ✅ debug后能独立解出     |      |  9'    |
| 9   | Zero Striping                                | Hash Map & Set              |NOK 需要in placing的解法      | 12'     |    7'  |
| 10  | Longest Consecutive Sequence                 | Hash Map & Set              |POK 只会加入sort的，不会不需要sort的      | 10'     | 4'      |
| 11  | Geometric Progression Triplets               | Hash Map & Set              |POK 大致能recall,还需要练习      |  15'    |  5'     |
| 12  | Reverse Linked List                          | Linked List                 | ✅     |      |    1'  |
| 13  | Remove Kth Node From End                     | Linked List                 | POK 可以做出，但未掌握快指针先走k步的算法     | 12'     |  5'     |
| 14  | Linked List Intersection                     | Linked List                 | NOK 完全不记得把两个链表连接起来的玩法了      | POK,判断条件不熟练 12.22; 15'     |   1' 純粹是剛複習過   |
| 15  | LRU Cache                                    | Linked List                 | ✅ 耗时较长，但已可以独立完成     |      | 25'     |
| 16  | Palindromic Linked List                      | Linked List                 | ✅     |      | 4'     |
| 17  | Flatten a Multi-Level Linked List            | Linked List       | ✅     |      |  4'    |
| 18  | Linked List Loop          | Fast And Slow Pointers      |   ✅     |      |  1'    |
| 19  | Linked List Midpoint            | Fast And Slow Pointers      |✅  利用dummy的话，最好使用while fast.next and fast.next.next     |      |  2'    |
| 20  | Happy Number            | Fast And Slow Pointers      | ✅     |      |  8'     |
| 21  | Substring Anagrams            | Sliding window                        | POK 能回想起来怎么做，但最好再练练    | 25'     |      |
| 22  | Longest Substring with Unique Characters            | Sliding window                        |✅   |      |  5'    |
| 23  | Longest Uniform Substring After Replacements        | Sliding window                        |NOK 12.10 全忘了。静态窗口和动态窗口最大的区别在于后者窗口的大小会动态变化.动态窗口的right一般在循环的最后+1 | 12'     |   6'   |
| 24  | Find the Insertion Index            | Binary Search                        |POK while left < right 是让left和right merge成为一个值，而left <= right则是让 right越过left. left or right = mid + 1 or mid, 则是决定是否把mid作为答案之一的选择，right最大值的选择也要看是否包含n; 而mid = (left + right) // 2后面是否+1, 则决定把mid往left还是right推|  12'    |  3'    |
| 25  | First and Last Occurrences of a Number            | Binary Search                        | NOK 12.10 mid 加减1以及不加减1的妙用，确定了上bound和下bound的走向     |  25'    |   12' 还是有点不熟练   |
| 26  | Cutting Wood           | Binary Search                       | ✅     |      |   10'   |
| 27  | Find the Target in a Rotated Sorted Array            | Binary Search                       | NOK 12.10 永远在左或右中某个有序的array中继续搜索    |  POK 12.22 ; 10'   |  14'    |
| 28  | Find the Median From Two Sorted Arrays           | Binary Search                       | NOK 12.10 只记得基本的结构，1.确保短的arr在前 2.L1_index为nums1的mid,(L2_index+1)+(L1_index+1)=(len(nums1)+len(nums2))/2 3.通过L1_index和L2_index把两个数组平分 4.确定L1,R1,L2,R2四个值,单个数组可能用光的情况时L=-inf,R=inf 5.当L1>R2时,说明nums1太右,right往左移 6.当L2>R1时,说明nums1太小,left往右移 7.调整后根据数组总长度的奇偶性计算中位数    | POK mid2的选择有问题。需要使得左分部的值的个数总是小于或等于右半部分，如果只有一个中位数，也是去右面的数组取; 8'    |   10'   |
| 29  | Matrix Search            | Binary Search                       | ✅     |      |  12'    |
| 30  | Local Maxima in Array            | Binary Search                        | NOK, 12.11 局部求一个极值，窍门是更右面的值比较，如果右面的值大于mid,则mid不可能是极值，所以left取mid+1； 如果右值小于mid,意味着mid可能是极值，所以right取mid     |  5'    |  2'     |
| 31  | Weighted Random Selection            | Binary Search                        | NOK, 12.11 先根输入的weight数组，形成一个sum后的数组，size和输入的相同   # 然后用randint生成一个介于1和最大sum之间的随机数，通过left和right来寻找可以插入这个target的位置，并返回索引 | 20' looking for the lower-bound prefix sum which satisfies the condition prefix_sums[mid] ≥ target.     | 10'     |
| 32  | Valid Parenthesis Expresssion            | Stacks                       |  ✅    |      |  3'    |
| 33  | Next Largest Number to the Right            |  Stacks                      |✅      |      |  3'    |
| 34  | Evaluate Expression            | Stacks                       | ✅     |      |  12'    |
| 35  | Repeated Removal of Adjacent Duplicates            |  Stacks                      |✅      |      |  5'    |
| 36  | Implement a Queue using Stacks            |  Stacks                      | ✅     |      |   5'   |
| 37  | Maximums of Sliding Window            |  Stacks                     | ✅ 对于下标和k的关系，可以列方程或不等式来解决    |      |   8'   |
| 38  | K Most Frequent Strings            |  Heaps                      | ✅    |      |   6'   |
| 39  | Combine Sorted Linked Lists            |  Heaps                     |POK, 一方面是忘了个class直接注入lambda的作法，dummy处理head的也不够熟练     | 8'     |   3'   |
| 40  | Median of an Integer Stream            |  Heaps                      |✅ 除了heap[0]表示栈顶，其他都记得很清楚     |      |   10'   |
| 41  | Sort a K-sorted Array            |  Heaps                      | ✅    |      |  5'    |
| 42  | Merge Overlapping Intervals            | Intervals                       | ✅    |      |  5'     |
| 43  | Identify All Interval Overlaps            | Intervals                       | ✅ debug后能自己想出来    |      |      |
| 44  | Largest Overlap of Intervals            | Intervals                       | ✅    |      |  6'    |
| 45  | Sum Between Range            |  Prefix Sums                      | ✅    |      |   3'   |
| 46  | K-Sum Subarrays            |  Prefix Sums                       | NOK 12.15 运用presum + hash    |  NOK pre_sum - another_pre_sum == k    |   2'   |
| 47  | Product Array Without Current Element             |  Prefix Sums                       | ✅      |      |  5'    |
| 48  | Invert Binary Tree            |  Trees                      | ✅      |      |  2' 递归算法  2' stack算法  |
| 49  | Balanced Binary Tree Validation             | Trees                       | ✅      |      |  5'    |
| 50  | Rightmost Nodes of Binary Tree            | Trees                       |  ✅    |      |   1'30''   |
| 51  | Widest Binary Tree Level            | Trees                       | ✅     |      |      |
| 52  |Binary Search Tree Validation             | Trees                       | ✅      |      |   5'   | 
| 53  | Lowest Common Ancestor            | Trees                       |  ✅    |      | 5'     |
| 54  |  Build Binary Tree From Preorder and Inorder Traversals           | Trees                       |✅      |      |  不会做了    |
| 55  | Maximum Sum of a Continuous Path in a Binary Tree            | Trees                       | ✅     |      |  6'    |
| 56  | Binary Tree Symmetry            | Trees                      | ✅    |      |  3'    |
| 57  | Binary Tree Columns            | Trees                       | ✅    |      |  8'    |
| 58  | Kth Smallest Number in a Binary Search Tree            | Trees                       | ✅    |      |   12'   |
| 59  | Serialize and Deserialize a Binary Tree            | Trees                       |✅ 原解更推荐使用iter和next的搭配，这个global取得的效果是类似的；返回字符串之前可以先放在list里，然后再统一join返回     |      |  15'    |
| 60  | Design a Trie            |  Tries                      | ✅     |      |   8'   |
| 61  | Insert and Search Words with Wildcards            |  Tries                      | ✅       |      |   21'   |
| 62  | Find All words on a Board            |  Tries                      |✅  注意把tries归位，以及不要找到一个就return了    |      |   20'   |
| 63  | Graph Deep Copy            |  Graphs                      | ✅     |      |   2'   |
| 64  | Cound Islands            |  Graphs                      |  ✅    |      |    5'  |
| 65  | Matrix Infection           |  Graphs                      |   ✅   |      |   10'   |
| 66  | Bipartite Graph Validation            |  Graphs                      |  ✅    |      |  5'    |
| 67  | Longest Increasing Path            |  Graphs                      |  ✅    |      | 7'     |
| 68  | Shortest Transformation Sequence            |  Graphs                      | POK 12.17 一些访问和计数的细节掌握的不好    | 10'     |   8'   |
| 69  | Merging Communities            |  Graphs                      | POK 12.17 find递归查找有点记不清了   |  6'    |  4'    |
| 70  | Prerequisites            |  Graphs                      | ✅     |      |  6'    |
| 71  | Shortest Path            |  Graphs                      | NOK 12.17 放进heap里面的distance是总的距离，不是单个点对点的weight    | 12'     |  10' 我是把所有的新边都放进了heap,但实际上只要放入新缩减的距离和节点即可    |
| 72  | Connect the Dots            |  Graphs                      | ✅     |      |   17'   |
| 73  | Find All permutations            | Backtracking                        |✅      |      |   15'  |
| 74  | Find All Subsets            | Backtracking                       | ✅     |      |   15' 不够熟   |
| 75  | N Queens            | Backtracking                       | ✅ Permutation和Combination都需要去除（回溯）后，但P回溯后不需要直接在循环里二次调用，而Combination是在循环里回溯后继续调用，从这一点上而言，N皇后是一个排列而不是组合    |      |      |
| 76  | Combinations of a Sum            | Backtracking                       | ✅     |      |   NOK 这个有点忘了，8'  |
| 77  | Phone Keypad Combinations            | Backtracking                       | ✅     |      |   6'   |
| 78  | Climbing Stairs            | Dynamic Programming                       | ✅     |      |  1'    |
| 79  | Minumum Coin Combination            | Dynamic Programming                       | ✅     |      |   4'   |
| 80  | Matrix Pathways            | Dynamic Programming                       | ✅ 特例只使用两个row的情况还需要练习     |      |  4'    |
| 81  | Neighborhood Burglary            | Dynamic Programming                       | ✅    |      | 3'     |
| 82  | Longest Common Subsequence            | Dynamic Programming                       |✅     |      |  20' 有点 忘了    |
| 83  | Longest Palindrome in a String            | Dynamic Programming                       | ✅ 在根据substring的长度循环时，需要注意n - sublen == 0时其实还是需要遍历的，因此range里面要+1    |      |  15'    |
| 84  | Maximum Subarray Sum            | Dynamic Programming                       | POK 12.18 记得大概但忘了最后是取dp里面的最大值    |  3'    |   2'   |
| 85  | 0/1 knapsack            | Dynamic Programming                       | ✅ 非常NB    |      |  15' 有点小错误了    |
| 86  | Largest Square in a Matrix            | Dynamic Programming                       | ✅     |      |  7'    |
| 87  | Jump the the End            | Greedy                       | NOK 12.18 每次只找满足条件的上一个目的地，不满足的会循环跳过。dp也能用于解决此问题  | 10' 很小的一道题目，花了不少时间，还是不太熟练; 再做3'      |  2'     |
| 88  | Gas Stations            | Greedy                       | ✅     |      |      |
| 89  | Candies            | Greedy                       |  ✅      |      |  4'    |
| 90  | Sort linked List            | Sort And Search                       |  ✅ while fast.next and fast.next.next是用于让slow指向左中点，而fast and fast.next则会让slow指向右中点      |     |  10'    |
| 91  | Sort Array            | Sort And Search                       | ✅  quick sort NB, merge sort不太熟悉了，quick sort只有一个split两个递归，merge除了一个split两个递归，最后还有一个merge    |      |  12    |
| 92  | Kth Largest Integer            | Sort And Search                       |  ✅    |      |  3'    |
| 93  | Dutch National Flag            | Sort And Search                       | ✅ 原著使用的交换方法也值得学习，可得交换算法精髓    |      |   10' 使用了新的swap方法   |
| 94  | Hamming Weights of Integers            | Bit Manipulation                       |  ✅    |      |   1'   |
| 95  | Lonely Integer            | Bit Manipulation                       | ✅     |      |      |
| 96  | Swap Odd and Even Bits            | Bit Manipulation                       | ✅    |       |   1'   |
| 97  | Spiral Traversal            | Math and Geometry                       | POK 12.19 第三第四个循环的if条件还掌握的不熟    |  10'    |   9'   |
| 98  | Reverse 32-Bit Integer            | Math and Geometry                       | POK math.fmod(n, 10) 未掌握，这个余数的符号与被除数一致，如果要运用%求负数的模，可以把 a % b 里面的b的符号进行修改    |  3'    |   3'   |
| 99  | Maximum Collinear Points            | Math and Geometry                       | POK 掌握的还不错，但遗漏了关键的map或者说分割是要按focus为前置的键的 | 10'     |   8'   |
| 100  | The Josephus Problem            | Math and Geometry                       | NOK    |  3'    |   1' + 1'   |
| 101  | Trangle Numbers            | Math and Geometry                       | ✅      |      |    6'  |

### First Round Redo:

40: 7 POK, 9 NOK, 24 OK  
60: 7 POK, 10 NOK, 43 OK  
80: 9 POK, 11 NOK, 60 OK  
101: 13 POK, 13 NOK, 75 OK  

In the first round, it took me about 193 tomatos to complete all the practice.  
In the second round, it only took me about one-third of the time in the first round.   