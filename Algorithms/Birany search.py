"""
  	Binary search is a search algorithm that finds the position of a target value within a sorted array.
  	Binary search compares the target value to the middle element of the array; if they are unequal,
  	the half in which the target cannot lie is eliminated and the search continues on the remaining half until it is successful.
  	If the search ends with the remaining half being empty, the target is not in the array.
	Binary search runs in at worst logarithmic time, making O(log n) comparisons, where n is the number of elements in the array.
"""

def binarySearchIteratively(tabOfElems, searchedValue):
	start = 0
	end = len(tabOfElems) - 1

	while True:
		if start > end:
			return None

		mid = int((start + end) / 2)
		# print start, mid, end

		if (tabOfElems[mid] < searchedValue):
			start = mid + 1
		elif (tabOfElems[mid] > searchedValue):
			end = mid - 1
		else:
			return mid

def bsRec(tabOfElems, searchedValue):
	return bsRecInner(tabOfElems, searchedValue, 0, len(tabOfElems))

def bsRecInner(tabOfElems, searchedValue, start, end):
	if start >= end:
		return None

	mid = int((start + end) / 2)

	if (searchedValue > tabOfElems[mid]):
		return bsRecInner(tabOfElems, searchedValue, mid + 1, end)
	elif (searchedValue < tabOfElems[mid]):
		return bsRecInner(tabOfElems, searchedValue, start, mid)
	else:
		return mid


def binarySearchVariantFindingMinimum(tabOfElems, start, end):

	mid = start + (end - start) / 2

	if (start > end):
		return NOT_FOUND

	if(start == end):
		return mid

	if (mid > start and tabOfElems[mid] < tabOfElems[mid - 1]):
		return mid

	if(mid < end and tabOfElems[mid] > tabOfElems[mid + 1]):
		return mid + 1

	elif(tabOfElems[mid] < tabOfElems[end]):
		return binarySearchVariantFindingMinimum(tabOfElems, start, end)
	else:
		return binarySearchVariantFindingMinimum(tabOfElems, mid + 1, end)

def interpolationSearch(tabOfElems, searchedValue):

	start = 0
	end = len(tabOfElems)
	end = end - 1


	while (start < end):
		mid = start + ((end - start) / (tabOfElems[end] - tabOfElems[start])) * (searchedValue - tabOfElems[start])

		if (tabOfElems[mid] < searchedValue):
			start = mid + 1
		elif (searchedValue < tabOfElems[mid]):
			end = mid - 1
		else:
			return mid

	return NOT_FOUND

def test(tab, fun):
	pass

def bsFun(tab, elem, startIndex):
	if not tab:
		return None

	mid = int(len(tab) / 2)
	# print tab, mid

	if elem < tab[mid]:
		return bsFun(tab[ : mid], elem, startIndex)
	elif elem > tab[mid]:
		return bsFun(tab[mid + 1 : ], elem, startIndex + mid + 1)
	else:
		return startIndex + mid

def main():
	tab = [1, 9, 14, 66, 75, 77, 83, 97]
	tab.sort()

	# res = binarySearchIteratively(tab, 96)
	print(bsFun(tab, 15, 0))
	print(bsFun(tab, 1, 0))
	print(bsFun(tab, 97, 0))
	print(bsFun(tab, 77, 0))

	# print res
	# if res:
	# 	print tab[res]

	# start = 0
	# end = len(tab)
	# print(binarySearchRecursive(tab, 97, start, end))

	# print(end)
	# tmpEnd = end - 1
	# print(tmpEnd)
	# #print(binarySearchVariantFindingMinimum(tab, start, tmpEnd))

	# print(interpolationSearch(tab, 14))

if __name__ == "__main__":
	main()
