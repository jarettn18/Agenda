"""
Author: Jarett Nishijo

Defines expressions and basic math functions
#Used in rpncalc.py
"""
# One global environment (scope) for
# the calculator

ENV = dict()

def env_clear():
    """Clear all variables in calculator memory"""
    global ENV
    ENV = dict()

class Expr:
    """Abstract base class of all expressions."""

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        raise NotImplementedError("Each concrete Expr class must define 'eval'")

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        raise NotImplementedError("Each concrete Expr class must define __str__")

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        raise NotImplementedError("Each concrete Expr class must define __repr__")

class IntConst(Expr):

    def __init__(self, value):
        self.value = value

    def eval(self) -> "IntConst":
        return self

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"IntConst({self.value})"

    def __eq__(self, other: Expr) -> bool:
        return isinstance(other, IntConst) and self.value == other.value


class BinOp(Expr):
    """Abstract base class for binary operators +, *, /, -"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self) -> "IntConst":
        """Each concrete subclass must define _apply(int, int)->int"""
        left_val = self.left.eval()
        right_val = self.right.eval()
        return IntConst(self._apply(left_val.value, right_val.value))

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return f"({str(self.left)} {self.opsym} {str(self.right)})"

    def __repr__(self) -> str:
        return f"{self.wordop}({repr(self.left)}, {repr(self.right)})"

    def __eq__(self, other: "Expr") -> bool:
        return type(self) == type(other) and \
               self.left == other.left and \
               self.right == other.right

class Plus(BinOp):
    """left + right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "+"
        self.wordop = "Plus"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int, right: int) -> int:
        return left + right

class Times(BinOp):
    """left * right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "*"
        self.wordop = "Times"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int, right: int) -> int:
        return left * right

class Div(BinOp):
    """left / right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "/"
        self.wordop = "Div"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int, right: int) -> int:
        return left // right

class Minus(BinOp):
    """Left - Right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "-"
        self.wordop = "Minus"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int, right: int) -> int:
        return left - right

class Remainder(BinOp):
    """Left % Right"""

    def __init__(self, left: Expr, right: Expr):
        super().__init__(left, right)
        self.opsym = "%"
        self.wordop = "Remainder"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int, right: int) -> int:
        return left % right


class UnOp(Expr):

    def __init__(self, left):
        self.left = left

    def eval(self):
        left_val = self.left.eval()
        return IntConst(self._apply(left_val.value))

    def __str__(self):
        return f"({str(self.left)} {self.opsym})"

    def __repr__(self) -> str:
        return f"{self.wordop}({repr(self.left)})"

    def __eq__(self, other: "Expr") -> bool:
        return type(self) == type(other) and \
               self.left == other.left

class Abs(UnOp):
    """left abs"""

    def __init__(self, left: Expr):
        super().__init__(left)
        self.opsym = "@"
        self.wordop = "Abs"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int) -> int:
        return abs(left)


class Neg(UnOp):
    """left neg"""

    def __init__(self, left: Expr):
        super().__init__(left)
        self.opsym = "~"
        self.wordop = "Neg"

    def eval(self) -> "IntConst":
        """Implementations of eval should return an integer constant."""
        return super().eval()

    def __str__(self) -> str:
        """Implementations of __str__ should return the expression in algebraic notation"""
        return super().__str__()

    def __repr__(self) -> str:
        """Implementations of __repr__ should return a string that looks like
        the constructor, e.g., Plus(IntConst(5), IntConst(4))
        """
        return super().__repr__()

    def __eq__(self, other):
        return super().__eq__(self, other)

    def _apply(self, left: int) -> int:
        return left * -1

class Var(Expr):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Var({self.name})"

    def eval(self):
        global ENV
        if self.name in ENV:
            return ENV[self.name]
        else:
            raise UndefinedVariable(f"{self.name} has not been assigned a value")

    def assign(self, value: IntConst):
        ENV[self.name] = value

class Assign(Expr):
    """Assignment:  x = E represented as Assign(x, E)"""

    def __init__(self, left: Var, right: Expr):
        assert isinstance(left, Var)  # Can only assign to variables!
        self.left = left
        self.right = right

    def eval(self) -> IntConst:
        r_val = self.right.eval()
        self.left.assign(r_val)
        return r_val

    def __str__(self) -> str:
        return f"{str(self.left)} = {str(self.right)}"

    def __repr__(self) -> str:
        return f"Assign({repr(self.left)}, {repr(self.right)})"

class UndefinedVariable(Exception):
    """Raised when expression tries to use a variable that
    is not in ENV
    """
    pass