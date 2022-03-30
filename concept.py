class SuperParent:

    def super_parent_func(self, sp):
        return sp


class ChildA(SuperParent):

    def child_a_func(self, ca):
        return ca

    def _a_super_parent_func(self, sp):
        return self.super_parent_func(sp)


class ChildBX(SuperParent):

    # DOES NOT EXIST in MRO for ChildBX objects
    def super_parent_func(self, ca):
        pass


class ChildB(SuperParent):

    def child_b_func(self, cb):
        return cb

    def _b_super_parent_func(self, sp):
        return self.super_parent_func(sp)


class SuperChild(ChildA, ChildB):

    def super_child_func(self, sc):
        return sc

    def _a_super_parent_func_upper(self, sp):
        return str(self._a_super_parent_func(sp)).upper()

    def _b_super_parent_func_lower(self, sp):
        return str(self._b_super_parent_func(sp)).lower()

    def child_ab_func(self, ca, cb):
        return str(self.child_a_func(ca)) + str(self.child_b_func(cb))


sp = "SuperParent"
ca = "ChildA"
cb = "ChildB"
sc = "SuperChild"


# SuperParent
value_1 = 44
value_2 = 67
super_parent = SuperParent()
super_parent_func = super_parent.super_parent_func("'SuperParent' method from 'SuperParent class")



# ChildA
child_a = ChildA()
child_a_func = child_a.child_a_func("'ChildA' method from 'ChildA' class")
_a_super_parent_func = child_a._a_super_parent_func(ca)
print(_a_super_parent_func)
#print(type(_a_super_parent_func))


# ChildB
child_b = ChildB()
child_b_func = child_b.child_b_func("'ChildB' method from 'ChildB' class")
_b_super_parent_func = ChildB()._b_super_parent_func(cb)
#print(child_b_func)
#print(_b_super_parent_func)


# SuperChild
super_child = SuperChild()
super_child_func = super_child.super_child_func("Super Child' method from 'ChildB class")
super_child_func_upper = SuperChild()._a_super_parent_func_upper(sp)
super_child_func_lower = SuperChild()._b_super_parent_func_lower(sp)
child_ab_func = SuperChild().child_ab_func(ca, cb)
#print(super_child_func)
#print(super_child_func_upper)
#print(super_child_func_lower)
#print(child_ab_func)