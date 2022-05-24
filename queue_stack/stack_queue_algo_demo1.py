from queue_stack.order_stack_demo1 import OrderStack


class Solution:
    def tran_dec_to_bin(self, dec_num):
        if dec_num <= 0:
            return
        result_stack = OrderStack()
        n = dec_num
        while n != 0:
            res = n % 2
            result_stack.push(res)
            n = n // 2

        result_str = ''
        num = result_stack.pop()
        while isinstance(num, int):
            result_str += str(num)
            num = result_stack.pop()

        return int(result_str)


if __name__ == '__main__':
    s = Solution()
    res = s.tran_dec_to_bin(11)
    print(res)
