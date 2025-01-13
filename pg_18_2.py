# class arithmatic

class arithmatic:
    def set_data(self, a, b):
        self.var_a = a
        self.var_b = b

    def addition(self):
        add = self.var_a + self.var_b
        return add
    
    def subtraction(self):
        sub = self.var_a - self.var_b
        return sub

arith_one = arithmatic()
arith_one.set_data(7, 5)
add_ret_one = arith_one.addition()
print(add_ret_one)

arith_two = arithmatic()
arith_two.set_data(9, 7)
sub_ret_two = arith_two.subtraction()
print(sub_ret_two)

arith_three = arithmatic()
arith_three.set_data(add_ret_one, sub_ret_two)
add_ret_three = arith_three.addition()
print(add_ret_three)

arith_four = arithmatic()
arith_four.set_data(add_ret_one, sub_ret_two)
add_ret_four = arith_four.subtraction()
print(add_ret_four)
