from maincode import fn1, Cl1
from nose.plugins.attrib import attr


@attr('unit')
def test_fn1():
    assert fn1() == 3


@attr('integration')
def test_cl1():
    class1 = Cl1(arg1='a')
    assert class1.args[0] == 'a'
