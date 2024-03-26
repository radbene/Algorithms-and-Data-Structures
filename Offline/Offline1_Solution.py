#Radosław Benedykciński
#Operation of the algorithm - for each element, the algorithm searches through the next k elements (less if we run out of the list earlier)
#the smallest of them is "clipped" to the beginning and then moves the pointer of the last element to the newly inserted element(to sort in ascending rather than descending order)
#algorithm has time complexity O(nk) and memory coplexity of O(1)
def SortH(p,k):
    l = Node()  #guardian
    l.next = p  #l becomes original list with a guardian for easy unclipping of first element
    H = begin = Node() #Head of sorted list
    H.val = H.next = None
    while l.next:   #Loop that checks if there are any elements left in l(except for guardian)
        i = 0   #counter for k next elements
        p = l.next  #l is now head of original list so p can now travel through the list
        mini = p.val
        prev=l  #pointer for previous element
        while p.next is not None and i < k: #Loop that searches for lowest value in k next elements(or until the end of a list)
            if p.next.val < mini:
                mini = p.next.val
                prev = p
            p = p.next
            i += 1
        x = prev.next   #unclipping element that has lowest value
        prev.next = x.next
        H.next = x  #clipping lowest value to the end of sorted list
        x.next = None   #detaching x from l
        H = H.next  #moving H to the newly clipped element(the current last element of the sorted list)
    return begin.next   #returning a pointer to the first element of the sorted list(it had a guardian so it returns guardian.next)
