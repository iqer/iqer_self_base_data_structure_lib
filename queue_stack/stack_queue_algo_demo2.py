from queue_stack.order_stack_demo1 import OrderStack


class Solution:
    def check_palindrome(self, str_info):
        if not len(str_info):
            return
        length = len(str_info)
        chars_list = list(str_info)

        is_odd = True if length % 2 == 1 else False
        to_push_count = length // 2
        s = OrderStack()

        for i in range(length):
            if i < to_push_count:
                s.push(chars_list[i])
            else:
                if is_odd and i == to_push_count:
                    continue
                item = s.pop()
                if item and item != chars_list[i]:
                    return False

        return True


if __name__ == '__main__':
    s1 = Solution()
    s_info = 'aaaa'
    print(s1.check_palindrome(s_info))
