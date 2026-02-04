class ListNode:

    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr_page = ListNode(homepage)
        self.head = self.curr_page
        self.tail = self.curr_page
        

    def visit(self, url: str) -> None:
        page = ListNode(url, prev=self.curr_page)

        # make the current pages next point here
        self.curr_page.next = page

        # # check if we're the tail node, update if so
        # if self.curr_page == self.tail: 
        self.tail = page
        # else:
        #     # if we're not the tail, we should be a valid node
        #     # assign the current pages next nodes previous pointer 
        #     # to this new node
        #     self.curr_page.next.prev = page

        # always update the current_page
        self.curr_page = page


    def back(self, steps: int) -> str:

        if self.curr_page == self.head:
            return self.curr_page.val

        i = 1

        while self.curr_page.prev:

            self.curr_page = self.curr_page.prev

            if i == steps:
                return self.curr_page.val

            i += 1

        # if we broke out, should be at head and will return head.
        return self.curr_page.val


    def forward(self, steps: int) -> str:

        if self.curr_page == self.tail:
            return self.curr_page.val

        i = 1

        while self.curr_page.next:

            self.curr_page = self.curr_page.next

            if i == steps:
                return self.curr_page.val

            i += 1

        # if we broke out, should be at tail.
        return self.curr_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)