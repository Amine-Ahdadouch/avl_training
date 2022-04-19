NB_ROT = 0

def reset_nb_rot():
        global NB_ROT
        NB_ROT = 0

class AVL_Node:
    def __init__(self, value) -> None:
        self._value = value
        self._left = None
        self._right = None
        self._balance = 0
    
    def getHeight(self):
        return max(self._left.getHeight() if self._left else -1, self._right.getHeight() if self._right else -1) + 1
    
    def rot_left(self):
        global NB_ROT
        NB_ROT += 1

        new_root = self._right
        self._right = new_root._left
        new_root._left = self

        new_root._balance = new_root.getbalance()
        return new_root

    def rot_right(self):
        global NB_ROT
        NB_ROT += 1

        new_root = self._left
        self._left = new_root._right
        new_root._right = self

        new_root._balance = new_root.getbalance()
        return new_root

    def getbalance(self):
        if not self:
            return 0
        return (self._left.getHeight() if self._left else -1) - (self._right.getHeight() if self._right else -1)
    
    def update_balance(self):
        self._left._balance = self._left.getbalance()
        self._right._balance = self._right.getbalance()

    def insert(self, val):
        if val < self._value:
            if self._left is None:
                self._left = AVL_Node(val)
            else:
                self._left.insert(val)
        elif val > self._value:
            if self._right is None:
                self._right = AVL_Node(val)
            else:
                self._right.insert(val)
        self._balance = self.getbalance()

        if self._balance > 1 and val < self._left._value:
            self = self.rot_right()
            self.update_balance()
        elif self._balance < -1 and val > self._right._value:
            self = self.rot_left()
            self.update_balance()
        elif self._balance > 1 and val > self._left._value:
            self._left = self._left.rot_left()
            self = self.rot_right()
            self.update_balance()
        elif self._balance < -1 and val < self._right._value:
            self._right = self._right.rot_right()
            self = self.rot_left()
            self.update_balance()
        return self
    
    def MinValue(self):
        if self is None or self._left is None:
            return self
        return self._left.MinValue()

    #Problem : can't delete root
    def delete(self, val):
        if self is None:
            return self
        elif val > self._value and self._right is not None:
            self._right = self._right.delete(val)
        elif val < self._value and self._left is not None:
            self._left = self._left.delete(val)
        else:
            if self._left is None:
                new_root = self._right
                self = None
                return new_root
            elif self._right is None:
                new_root = self._left
                self = None
                return new_root
            new_root = self._right.MinValue()
            self._value = new_root._value
            self._right = self._right.delete(val)
        
        self._balance = self.getbalance()

        if self._balance > 1 and self._left._balance >= 0:
            self = self.rot_right()
            self.update_balance()
        elif self._balance < -1 and self._right._balance <= 0:
            self = self.rot_left()
            self.update_balance()
        elif self._balance > 1 and self._left._value < 0:
            self._left = self._left.rot_left()
            self = self.rot_right()
            self.update_balance()
        elif self._balance < -1 and self._right._value > 0:
            self._right = self._right.rot_right()
            self = self.rot_left()
            self.update_balance()
        return self

    def print_tree(self):
        if not self:
            return None
        if self._left is not None:
            self._left.print_tree()
        print(self._value, self._balance)
        if self._right is not None:
            self._right.print_tree()
