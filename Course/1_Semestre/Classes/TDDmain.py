# from TDD import soma, triplo
import TDD as t

assert t.soma(2, 3) == 5
assert t.soma(10, 20) == 30

assert t.triplo(5) == 15
assert t.triplo(8) == 24

assert t.nickname("Eduardo Mendes") == "em76"

assert t.soPares([1,2,3,4,5,6,7,8,9]) == [2,4,6,8]
assert t.soPares([1,3,5,7]) == []