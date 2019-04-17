def permutate_int_list(in_list):
    temp_list = in_list
    for i in range(len(in_list)):
        for j in range(len(in_list)):
            temp_list[j], temp_list[i] = temp_list[i], temp_list[j]
            print(temp_list)

if __name__ == "__main__":
    permutate_int_list([1, 2, 3])
