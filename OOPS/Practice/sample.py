
def count_bits(var):
    num_bits = 0 
    while var:
        print(var)
        num_bits += var & 1
        var >>=1
    return num_bits

def swap_even(arr):
    even_index = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1
    return arr

def spiral_matrix():
    pass

if __name__ == "__main__":
    # num = count_bits(12)
    # print(num)
    ord_arr = swap_even([1,3,7,5,6,22])
    print(ord_arr) 