#Binary Search using Python

def bsf(arr,target):
	low=0
	high=len(arr)-1
	flag=0
	while (low<=high):
		mid=floor((start+end)/2)
		if (arr[mid]==target):
			flag=1
			pos=mid
		elif (arr[mid]>target):
			high=mid-1
		else:
			low=mid+1
			
	if flag==1:
		print("Element found at ",pos," position")
	else:
		print("Element Not Found")
	
	 
n=int(input("Enter the number of elements in the array :"))
arr=[]

#Input of Array
for i in range(0,n):
	ele=int(input("Enter the element :"))
	arr.append(ele)

#Displaying Sorted Array
arr.sort()
print("Sorted Array is :",*arr,sep=",")

target=int(input("Enter the element to be searched :"))
bsf(arr,target)

