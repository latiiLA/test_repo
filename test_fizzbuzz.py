from fizzbuzz import fizzbuzz

def test_fizzbuzz():
    output = fizzbuzz(15)
    
    expected = [
        1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
        11, "Fizz", 13, 14, "Fizz Buzz"
    ]

    assert output == expected, "FizzBuzz function output is incorrect"
