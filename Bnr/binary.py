import binascii
from unittest import result


def nibble_to_ascii(nibble: int) -> str:
  """
  This is a comment
  Input: Nibble (4-bits)
  Output: Single character HEX as a string
  Example: Input = 10, Output = 'A'
  Example: Input = 8,  Output = '8'
  """
  table = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  return table[nibble]


def to_hex(number: int) -> str:
    """
    This is a comment
    Input: Number (integer)
    Output: String
    Example: Input = 43605, Output = "0xAA55"
    """
    answer = ""
    
    # Forever loop
    while True:
        # Integer divide using the // operator
        quotient = number // 16
        # Get the remainder using the % operator
        remainder = number % 16
        
        
      #   Accumulate result
      #   Example: number = 41005
      #   Iteration 1 : Q = 2562, R = 13: Answer = D +""
      #   Iteration 2 : Q = 160, R = 2 : Answer = 2 + "D"
      #   Iteration 3 : Q = 10, R = 0: Answer = 0 + "2D"
      #   Iteration 4 : Q = 0 , R = 10 : Answer = A + "02D"
        
        # Accumulate result
        answer = nibble_to_ascii(remainder) + answer

        # Set the number we need to use for next time
        number = quotient
        
        # We break the "loop" when division turns to zero
        if (quotient == 0):
            break
    
    return "0x" + answer

def hextobin(hexval):
        '''
        we take the hex convert to binary . and return to value
        '''
        thelen = len(hexval)*4
        binval = bin(int(hexval, 16))[2:]
        while ((len(binval)) < thelen):
            binval = '0' + binval
        return binval

print(hextobin('7B316'))
print(to_hex(41005))
print(to_hex(0xA02D))
print(to_hex(0b1010000000101101))