# Q1. Write a program to find the second maximum GC value from the list also find the median GC value.
#     Gc values are as follows 30.5,12,54,23,84
# Answer
list1=[30.5, 12, 54, 23, 84]
list1.sort()
list1.reverse()

print(list1)
print(list1[1])
length=int(len(list1))
print(length)
if int(length)%2!=0 :
    median_odd=int((length+1)/2)
    print("The list contain odd no of value and median of the list is ", list1[median_odd-1])
else:
    median_1=int(length/2)
    median_2=int(length/2+1)
    median_even=float(int(list1[median_1-1])+int(list1[median_2-1]))/2
    print("The list contain the even no of items and median of the list is ", median_even)


# Q2. Write a program to check which stop codons are present in the sequence  â€œUAAAAGGCGAGAUAAAUAâ€.
# Q3. Check the presence of all the stop codons in the list ["UAA","UGC","AUAGCT","ATUA","UAG"] .
# Q4. Write a program to transcribe the sequence "ATGCTCGCGTAA"
# Q5. Concatenate two lists of GC Values [30.5,12,54,23,84] and [12,45,54,32] 
#     and find the maxium and minum GC Values.