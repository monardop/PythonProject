def mostBalancedPartition(parent, files_size):
    # Write your code here
    n = len(parent)
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parent[i]].append(i)
    size_sums = [None for _ in range(n)]
    
    def size_sums_rec(i):
        size_sums[i] = files_size[i] + sum(size_sums_rec(c) for c in children[i])
        return size_sums[i]
        
    size_sums_rec(0)
    return min(abs(size_sums[0] - 2 * ss) for ss in size_sums[1:])

            








mostBalancedPartition([-1,0,0,1,1,2], [1,2,2,1,1,1])
