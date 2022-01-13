import pytest

#MARK
@pytest.mark.prove_of_concept
def test_login():
    print('hello to the tester')

#FIXTURE(look at the conftest.py -- fixtures are stored in that file)
def test_fixture(supply_AA_BB_CC):
    zz = 25
    assert zz == supply_AA_BB_CC[0]

#PARAMETRIZE
#@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
#def test_add(input1, input2, output):
#	assert input1+input2 == output

def test_logoff():
    print('goodbye to the tester')

#SKIP TEST
@pytest.mark.skip
def test_good_morning():
    print('goodmorning tester')

def test_afternoon():
    print('good afternoon tester')

def test_calc():
    assert 2+2 == 4