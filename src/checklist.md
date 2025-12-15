|#   | Problem Name                                 | Category                    | Done |      |      |
|-----|----------------------------------------------|-----------------------------|------|------|------|
| 1   | Pair Sum - Sorted                            | Two Pointers                | ✅     |      |      |
| 2   | Triplet Sum                                  | Two Pointers                | POK 12.08     |      |      |
| 3   | Valid Palindrome                             | Two Pointers                | ✅     |      |      |
| 4   | Container With Most Water                    | Two Pointers                | ✅     |      |      |
| 5   | Move Zeroes                                  | Two Pointers                | NOK 12.09     |      |      |
| 6   | Next Lexicographical Sequence                | Two Pointers                | ✅ 稍欠火候      |      |      |
| 7   | Pair Sum - Unsorted                          | Hash Map & Set              | ✅      |      |      |
| 8   | Valid Sudoku                                 | Hash Map & Set              | ✅ debug后能独立解出     |      |      |
| 9   | Zero Striping                                | Hash Map & Set              |NOK 需要in placing的解法      |      |      |
| 10  | Longest Consecutive Sequence                 | Hash Map & Set              |POK 只会加入sort的，不会不需要sort的      |      |      |
| 11  | Geometric Progression Triplets               | Hash Map & Set              |POK 大致能recall,还需要练习      |      |      |
| 12  | Reverse Linked List                          | Linked List                 | ✅     |      |      |
| 13  | Remove Kth Node From End                     | Linked List                 | POK 可以做出，但未掌握快指针先走k步的算法     |      |      |
| 14  | Linked List Intersection                     | Linked List                 | NOK 完全不记得把两个链表连接起来的玩法了      |      |      |
| 15  | LRU Cache                                    | Linked List                 | ✅ 耗时较长，但已可以独立完成     |      |      |
| 16  | Palindromic Linked List                      | Linked List                 | ✅     |      |      |
| 17  | Flatten a Multi-Level Linked List            | Linked List       | ✅     |      |      |
| 18  | Linked List Loop          | Fast And Slow Pointers      |   ✅     |      |      |
| 19  | Linked List Midpoint            | Fast And Slow Pointers      |✅  利用dummy的话，最好使用while fast.next and fast.next.next     |      |      |
| 20  | Happy Number            | Fast And Slow Pointers      | ✅     |      |      |
| 21  | Substring Anagrams            | Sliding window                        | POK 能回想起来怎么做，但最好再练练    |      |      |
| 22  | Longest Substring with Unique Characters            | Sliding window                        |✅   |      |      |
| 23  | Longest Uniform Substring After Replacements        | Sliding window                        |NOK 12.10 全忘了。静态窗口和动态窗口最大的区别在于后者窗口的大小会动态变化.动态窗口的right一般在循环的最后+1 |      |      |
| 24  | Find the Insertion Index            | Binary Search                        |POK while left < right 是让left和right merge成为一个值，而left <= right则是让 right越过left. left or right = mid + 1 or mid, 则是决定是否把mid作为答案之一的选择，right最大值的选择也要看是否包含n; 而mid = (left + right) // 2后面是否+1, 则决定把mid往left还是right推|      |      |
| 25  | First and Last Occurentces of a Number            | Binary Search                        | NOK 12.10 mid 加减1以及不加减1的妙用，确定了上bound和下bound的走向     |      |      |
| 26  | Cutting Wood           | Binary Search                       | ✅     |      |      |
| 27  | Find the Target in a Rotated Sorted Array            | Binary Search                       | NOK 12.10 永远在左或右中某个有序的array中继续搜索    |      |      |
| 28  | Find the Median From Two Sorted Arrays           | Binary Search                       | NOK 12.10 只记得基本的结构，1.确保短的arr在前 2.L1_index为nums1的mid,(L2_index+1)+(L1_index+1)=(len(nums1)+len(nums2))/2 3.通过L1_index和L2_index把两个数组平分 4.确定L1,R1,L2,R2四个值,单个数组可能用光的情况时L=-inf,R=inf 5.当L1>R2时,说明nums1太右,right往左移 6.当L2>R1时,说明nums1太小,left往右移 7.调整后根据数组总长度的奇偶性计算中位数    |      |      |
| 29  | Matrix Search            | Binary Search                       | ✅     |      |      |
| 30  | Local Maxima in Array            | Binary Search                        | NOK, 12.11 局部求一个极值，窍门是更右面的值比较，如果右面的值大于mid,则mid不可能是极值，所以left取mid+1； 如果右值小于mid,意味着mid可能是极值，所以right取mid     |      |      |
| 31  | Weighted Random Selection            | Binary Search                        | NOK, 12.11 先根输入的weight数组，形成一个sum后的数组，size和输入的相同   # 然后用randint生成一个介于1和最大sum之间的随机数，通过left和right来寻找可以插入这个target的位置，并返回索引 |      |      |
| 32  | Valid Parenthesis Expresssion            | Stacks                       |  ✅    |      |      |
| 33  | Next Largest Number to the Right            |  Stacks                      |✅      |      |      |
| 34  | Evaluate Expression            | Stacks                       | ✅     |      |      |
| 35  | Repeated Removal of Adjacent Duplicates            |  Stacks                      |✅      |      |      |
| 36  | Implement a Queue using Stacks            |  Stacks                      | ✅     |      |      |
| 37  | Maximums of Sliding Window            |  Stacks                     | ✅ 对于下标和k的关系，可以列方程或不等式来解决    |      |      |
| 38  | K Most Frequent Strings            |  Heaps                      | ✅    |      |      |
| 39  | Combine Sorted Linked Lists            |  Heaps                     |POK, 一方面是忘了个class直接注入lambda的作法，dummy处理head的也不够熟练     |      |      |
| 40  | Median of an Integer Stream            |  Heaps                      |✅ 除了heap[0]表示栈顶，其他都记得很清楚     |      |      |
| 41  | Sort a K-sorted Array            |  Heaps                      | ✅    |      |      |
| 42  | Merge Overlapping Intervals            | Intervals                       | ✅    |      |      |
| 43  | Identify All Interval Overlaps            | Intervals                       | ✅ debug后能自己想出来    |      |      |
| 44  | Largest Overlap of Intervals            | Intervals                       | ✅    |      |      |
| 45  | Sum Between Range            |  Prefix Sums                      | ✅    |      |      |
| 46  | K-Sum Subarrays            |  Prefix Sums                       | NOK 12.15 运用presum + hash    |      |      |
| 47  | Product Array Without Current Element             |  Prefix Sums                       | ✅      |      |      |
| 48  | Invert Binary Tree            |  Trees                      | ✅      |      |      |
| 49  | Balanced Binary Tree Validation             | Trees                       | ✅      |      |      |
| 50  | Rightmost Nodes of Binary Tree            | Trees                       |     |      |      |
| 51  | Widest Binary Tree Level            | Trees                       |     |      |      |
| 52  |Binary Search Tree Validation             | Trees                       |     |      |      |
| 53  | Lowest Common Ancestor            | Trees                       |     |      |      |
| 54  |  Build Binary Tree From Preorder and Inorder Traversals           | Trees                       |     |      |      |
| 55  | Maximum Sum of a Continuous Path in a Binary Tree            | Trees                       |     |      |      |
| 56  | Binary Tree Symmetry            | Trees                      |     |      |      |
| 57  | Binary Tree Columns            | Trees                       |     |      |      |
| 58  | Kth Smallest Number in a Binary Search Tree            | Trees                       |     |      |      |
| 59  | Searialize and Deserialize a Binary Tree            | Trees                       |     |      |      |
| 60  | Design a Trie            |  Tries                      |     |      |      |
| 61  | Insert and Search Words with Wildcards            |  Tries                      |     |      |      |
| 62  | Find All words on a Board            |  Tries                      |     |      |      |
| 63  | Graph Deep Copy            |  Graphs                      |     |      |      |
| 64  | Cound Islands            |  Graphs                      |     |      |      |
| 65  | Matrix Infection           |  Graphs                      |     |      |      |
| 66  | Bipartite Graph Validation            |  Graphs                      |     |      |      |
| 67  | Longest Increasing Path            |  Graphs                      |     |      |      |
| 68  | Shortest Transformation Sequence            |  Graphs                      |     |      |      |
| 69  | Merging Communities            |  Graphs                      |     |      |      |
| 70  | Prerequisites            |  Graphs                      |     |      |      |
| 71  | Shortest Path            |  Graphs                      |     |      |      |
| 72  | Connect the Dots            |  Graphs                      |     |      |      |
| 73  | Find All permutations            | Backtracking                        |     |      |      |
| 74  | Find All Subsets            | Backtracking                       |     |      |      |
| 75  | N Queens            | Backtracking                       |     |      |      |
| 76  | Combinations of a Sum            | Backtracking                       |     |      |      |
| 77  | Phone Keypad Combinations            | Backtracking                       |     |      |      |
| 78  | Climbing Stairs            | Dynamic Programming                       |     |      |      |
| 79  | Minumum Coin Combination            | Dynamic Programming                       |     |      |      |
| 80  | Matrix Pathways            | Dynamic Programming                       |     |      |      |
| 81  | Neighborhood Burglary            | Dynamic Programming                       |     |      |      |
| 82  | Longest Common Subsequence            | Dynamic Programming                       |     |      |      |
| 83  | Longest Palindrome in a String            | Dynamic Programming                       |     |      |      |
| 84  | Maximum Subarray Sum            | Dynamic Programming                       |     |      |      |
| 85  | 0/1 knapsack            | Dynamic Programming                       |     |      |      |
| 86  | Largest Square in a Matrix            | Dynamic Programming                       |     |      |      |
| 87  | Jump the the End            | Greedy                       |     |      |      |
| 88  | Gas Stations            | Greedy                       |     |      |      |
| 89  | Candies            | Greedy                       |     |      |      |
| 90  | Sort linked List            | Sort And Search                       |     |      |      |
| 91  | Sort Array            | Sort And Search                       |     |      |      |
| 92  | Kth Largest Integer            | Sort And Search                       |     |      |      |
| 93  | Dutch National Flag            | Sort And Search                       |     |      |      |
| 94  | Hamming Weights of Integers            | Bit Manipulation                       |     |      |      |
| 95  | Lonely Integer            | Bit Manipulation                       |     |      |      |
| 96  | Swap Odd and Even Bits            | Bit Manipulation                       |     |      |      |
| 97  | Spiral Traversal            | Math and Geometry                       |     |      |      |
| 98  | Reverse 32-Bit Integer            | Math and Geometry                       |     |      |      |
| 99  | Maximum Collinear Points            | Math and Geometry                       |     |      |      |
| 100  | The Josephus Problem            | Math and Geometry                       |     |      |      |
| 101  | Trangle Numbers            | Math and Geometry                       |     |      |      |

### First Round Redo:

40: 7 POK, 9 NOK, 24 OK