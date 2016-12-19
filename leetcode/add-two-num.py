# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = None

        def _getVal(node):
        	if not node:
        		return 0
        	return node.val

        carry = 0
        while(l1 or l2 or carry):
        	sum = _getVal(l1) + _getVal(l2) + carry
        	val = sum % 10
        	carry = sum / 10
        	node = ListNode(val)
        	if not head:
        		head = tail = node
        	else:
        		tail.next = node
        		tail = node
        	if l1:
	        	l1 = l1.next
	        if l2:
	        	l2 = l2.next 

        return head


def createList(l):
	h = t = None
	for i in l:
		c = ListNode(i)
		if not h:
			h = t = c
		else:
			t.next = c
			t = c
	return h

def printList(l):
	print "--"
	while(l):
		print l.val
		l = l.next
	print "--"


l1 = createList([2,0,2])
l2 = createList([5,0,4,0])
printList(l1)
printList(l2)
x = Solution()
res = x.addTwoNumbers(l1,l2)
printList(res)










