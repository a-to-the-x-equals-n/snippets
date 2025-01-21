


def multiply_binary(I, J):


    """
    Divide and conquer algorithm for integer multiplication
    """
    # Convert binary strings to integers
    # num1 = int(I, 2)
    # num2 = int(J, 2)

    # Multiply the integers
    product = I * J


    # n = num of bits OR length of integer

    # I_h * J_h * 2 ** n + ((I_h - I_l)*(J_l - J_h) + (I_h * J_h) + (I_l * J_l)) * 2**(n//2) + (I_l * J_l)

    # Convert the product back to a binary string and return
    return bin(product)[2:]  # [2:] to strip the '0b' prefix



# Example usage
I_h = 0b0100  # I higher bound
I_l = 0b0001  # I lower bound

J_h = 0b1100 # J higher bound
J_l = 0b1111 # J lower bound



# print(f"The product of {bin1} and {bin2} is {multiply_binary(bin1, bin2)}")
print(f'{bin(I_h * J_h * 2 ** 8 + ((I_h - I_l)*(J_l - J_h) + (I_h * J_h) + (I_l * J_l)) * 2**(8//2) + (I_l * J_l))}')
















