def bigest_number_of_3(a,b,c):
    max_number_1 = max(a,b)
    max_number_2 = max(b,c)
    sum_of_numb = max_number_2 + max_number_1
    return sum_of_numb

print(bigest_number_of_3(1,2,3))

print(bigest_number_of_3(100,2,300))

print(bigest_number_of_3(100,-200,-300))