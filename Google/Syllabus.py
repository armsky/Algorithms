"""
Syllabus
1) Dynamic Programming
2) Super recursion (permutation, combination,...2^n, m^n, n!...etc. type of program. (NP hard, NP programs)
3) Probability related programs
4) Graphs: BFS/DFS are usually enough
5) All basic data structures from Arrays/Lists to circular queues, BSTs, Hash tables, B-Trees, and Red-Black trees, and all basic algorithms like sorting, binary search, median,...
6) Problem solving ability at a level similar to TopCoder Division 1, 250 points. If you can consistently solve these, then you are almost sure to get in with 2-weeks brush up.
7) Review all old interview questions in Glassdoor to get a feel. If you can solve 95% of them at home (including coding them up quickly and testing them out in a debugger + editor setup), you are in good shape.
8) Practice coding--write often and write a lot. If you can think of a solution, you should be able to code it easily...without much thought.
9) Very good to have for design interview: distributed systems knowledge and practical experience.
10) Good understanding of basic discrete math, computer architecture, basic math.
11) Coursera courses and assignments give a lot of what you need to know.
12) Note that all the above except the first 2 are useful in "real life" programming too!
"""

# Graphs
"""
Graphs are really important at Google. There are 3 basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list); familiarize yourself with each representation and its pros & cons. You should know the basic graph traversal algorithms: breadth‐first search and depth‐first search. Know their computational complexity, their tradeoffs, and how to implement them in real code. If you get a chance, try to study up on fancier algorithms, such as Dijkstra and A*
"""
# Advice
"""
And then start doing practice problems. You want this stuff to be intuitive so that you don't have to think about how to implement BFS. Implementing these more advanced algorithms is a good starting place, but don't let it be your sole source of preparation. I strongly recommend looking at Glassdoor and CareerCup and Interview Cake for more examples of actual questions that get asked. Cracking the Coding Interview is of course a great reference as well.

Dynamic programming is another thing you should practice. Yeah, you probably know it. You get it. But can you do it on the spot on a whiteboard for a problem you've never seen before without making mistakes? You need to get to that point, or at least reasonably close to it. The only way to do that is to just practice. Understanding is only half the equation. Speed is the other half.

Finally, keep in mind that probably at least one of your 6+ interviewers will ask you about operating systems or system design. In my opinion, those are the hardest questions by far to prepare for because there's just no "study list" for it. Interviewers can ask basically whatever they want, so you might even get a guy who wants you to just write huge regular expressions, or mess around with bit fiddling for 45 minutes. The unpredictability of it all certainly sucks, but my advice is to be prepared not just for the core data structures and algorithms but also off-the-beaten-path topics like those I just mentioned.
"""

# From recruiter
"""
Big-O notations also known as "the run time characteristic of an algorithm".  You may want to refresh hash tables, heaps, binary trees, linked lists, depth-first search, recursion. For more information on Algorithms you can visit:

http://www.topcoder.com/tc?odule=Static&d1=tutorials&d2=alg_index

Coding: You should know at least one programming language really well (preferably C++,  Java or Python). You will be expected to write some code in at least some of your interviews. You will be expected to know a fair amount of detail about your preferred programming language and will be asked to do some coding on the whiteboard.

Sorting: Know how to sort. Don't do bubble-sort. You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quicksort and merge sort). Merge sort can be highly useful in situations where quick sort is impractical, so take a look at it.

Hashtables: Arguably the single most important data structure known to mankind. You absolutely should know how they work. Be able to implement one using only arrays in your favorite language, in about the space of one interview.

Trees: Know about trees; basic tree construction, traversal and manipulation algorithms. Familiarize yourself with binary trees, n-ary trees, and trie-trees. Be familiar with at least one type of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree, and know how it's implemented. Understand tree traversal Algorithms: BFS and DFS, and know the difference between inorder, postorder and preorder.

Graphs: Graphs are really important at Google. There are 3 basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list); familiarize yourself with each representation and its pros & cons. You should know the basic graph traversal algorithms: breadth-first search and depth-first search. Know their computational complexity, their tradeoffs, and how to implement them in real code. If you get a chance, try to study up on fancier algorithms, such as Dijkstra and A*.

Other Data Structures: You should study up on as many other data structures and algorithms as possible. You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise. Find out whatNP-complete means.

Mathematics: Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other companies because counting problems, probability problems, and other Discrete Math 101 situations surrounds us. Spend some time before theinterview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability. You should be familiar with n-choose-k problems and their ilk – the more the better.

Operating Systems: Know about processes, threads and concurrency issues. Know about locks and mutexes and semaphores and monitors and how they work. Know about deadlock and livelock and how to avoid them. Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware. Know a little about scheduling. The world is rapidly moving towards multi-core, so know the fundamentals of "modern" concurrency constructs.
"""
