from modulemeta import Module


class Wat(metaclass=Module):
  'Waat'

  _ermelon = 5
  arr = [1, 2, 3]

  def ermelon():  # type: ignore[misc] # mypy thinks this is a method
    return _ermelon  # noqa


class Wat2(metaclass=Wat):  # type: ignore[misc]  # `Wat` is not a `type`
  'Waat2'

  _ermelon = 7


def test_wat_name():
  assert Wat.__name__ == 'Wat'


def test_wat2_name():
  assert Wat2.__name__ == 'Wat2'


def test_wat_doc():
  assert Wat.__doc__ == 'Waat'


def test_wat2_doc():
  assert Wat2.__doc__ == 'Waat2'


def test_wat_repr():
  assert str(Wat) == "<module 'Wat'>"


def test_wat2_repr():
  assert str(Wat2) == "<module 'Wat2'>"


def test_wat_primitive():
  assert Wat.ermelon() == 5


def test_wat2_primitive():
  assert Wat2.ermelon() == 7


def test_arr():
  Wat2.arr.append(4)
  assert Wat2.arr == [1, 2, 3, 4]
  assert Wat.arr == [1, 2, 3]
