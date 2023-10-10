 # triple A pattern
# arrange
# act
# assert

def add(x, y):
    return x + y


def test_add__when_1_and_2__expect_3():
    # arrannge
    expected = 3
    # act
    actual = add(1, 2)
    # assert
    if actual == expected:
        print('OK')
    else:
        print('Wrong')

def test_add__when_2_and_1__expect_3():
    expected = 3
    actual = add(2, 1)
    if actual == expected:
        print('OK')
    else:
        print('Wrong')

test_add__when_1_and_2__expect_3()
test_add__when_2_and_1__expect_3()


    


# 1, 2 - 3
# 2, 1 - 3
