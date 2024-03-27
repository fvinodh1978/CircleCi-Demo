
import sys

# adding src to the system path
sys.path.insert(0, '/home/circleci/circleci-python/src')
from main import add, product, division

def test_add():
    assert add(5, 5)==10
    print("Add Test : Add Function Works Correctly")

def test_product():
    assert product(5, 5)==25
    print("Add Test : product Function Works Correctly")

def test_division():
    assert product(5, 5)==1
    print("Add Test : Division Function Works Correctly")    

if __name__ =='__main__':
    test_add()
    test_product()
    test_division()