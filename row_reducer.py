#row_reducer.py is the file name
#import libraries here
import pandas as pd
import numpy as np

def jordan_concat(mat):
	#create identity ndarray with numpy
	identity_ndarr=np.identity(mat.shape[0])
	#convert it into a dataframe in pandas
	identity_df = pd.DataFrame(np.identity(3))
	#return their concatenation
	return pd.concat(objs=[mat, identity_df], axis='columns', ignore_index=True)

def swaprows(mat, idx1, idx2):
	temp_row = np.copy(mat[idx1])
	mat[idx1] = mat[idx2]
	mat[idx2] = temp_row
	return mat

def check_pivots(mat, indx1, indx2):
	#this will check pivots not zero
	for i in range(mat.shape[0]):
		if mat[i][i]==0:
			mat = swaprows(mat,indx1, indx2)
	return

def to_upper_tri(mat):
	#convert the dataframe to numpy for easier row access and arithmetic
	#row i contains the pivot here
	for i in range(mat.shape[0]):#assumes matrix is square m=n
		select_row=mat[i]
		#print('row 1, pivot is ', select_row[i], 'at index ', i)
		#print('pivot row is ', select_row)
		for j in range(mat.shape[0]):
			#if comparison row is above pivot row
			if j<i:
				pivot_row = mat[j]
				#find multiple for pivot elimination
				multiple = mat[i][j] / mat[j][j]
				#print(multiple)
				new_row = select_row - (multiple * pivot_row)
				#print(new_row)
				mat[i]= new_row
				print(mat)
	return mat

def to_diagonal(mat):
	for i in range(mat.shape[0]):
		last_indx = mat.shape[0]-1-i
		last_row = mat[last_indx]
		for j in range(mat.shape[0]):
			if j < last_indx:
				multiple = mat[j,last_indx] / mat[last_indx][last_indx]
				new_row = mat[j] - (multiple * last_row)
				mat[j] = new_row
				print(mat)
	return mat

def to_IdInv(mat):
	for i in range(mat.shape[0]):
		if mat[i][i] != 0:
			multiple = mat[i][i]
			new_row = mat[i] / multiple
			mat[i] = new_row
	return mat

def main():
	matr=pd.read_csv("mat.txt")
	jordy = jordan_concat(matr)
	print(jordy)
	print('performing elimination...')
	jordy = jordy.to_numpy()
	upp_tri = to_upper_tri(jordy)
	diag = to_diagonal(upp_tri)
	answer = to_IdInv(diag)
	#reduced = to_upper_tri(jordy)
	#print('answer...')
	print(answer[0:jordy.shape[0],jordy.shape[0]:jordy.shape[0]*2])
	return



if __name__ == "__main__":
	main()






















#read csv provided in same directory

#this function checks if the matrix is invertible
'''
def is_invertible(mat):
	#check here that the matrix is square
	if not mat.shape[0]==mat.shape[1]:
		return False
	"""
	check here linear independence of columns.
	we have M columns and we check linear independence 
	for eachpair of two, so that is a combination 
	problem in which we have M!/((2!)(M-2)!) iterations
	"""
	for i in range(mat.shape[0]):
		for j in range(mat.shape[0]):
			if j>i:
			#the inequality ensures no repeats 
			#and no comparing a col to itself
				col1=mat.iloc[:,i]
				col2=mat.iloc[:,j]
				if not are_linearly_independent(col1, col2):
					print("I found a pair of linearly dependant columns...")
					return False
	print("no linearly dependent columns found...")
	print("matrix is invertible...")
	return True


#this compares two columns from the matrix
#to check if they are linearly independent
def are_linearly_independent(column1, column2):
	if column1.iloc[0]>=column2.iloc[0]:
		bigger_first_elem=column1
		smaller_first_elem=column1
		multiple=column1.iloc[0]/column2.iloc[0]
	else:
		bigger_first_elem=column2
		smaller_first_elem=column1
		multiple=column2.iloc[0]/column1.iloc[0]
	test_equiv=smaller_first_elem.multiply(multiple)
	#check if the row is a multiple of the other
	#by comparing each element aside from the first
	
	for i in range(column1.shape[0]-1):
		if not bigger_first_elem.iloc[i+1]==test_equiv.iloc[i+1]:
			print("rows linearly dep by " + str(multiple) +"...")
			return True
	return False

'''
"""
We would be equally fine if we return the idea
that they are the linearly independent or
linearly dependent as long as it is consistent. 
After some thought the more logical choice is 
to return if the columns are linearly independent.
This way we may assume one is a multiple of 
the other (is linearly dependent) and we would
be alerted if the opposite is true. It only takes
one difference to find out if they are not multiples
instead of checking all entries to find out if they
are multiples. If we find an inconsistency in 
corresponding elements, we immediately return true
and know the columns are linearly independent.
"""


#concatenate matrix with identity of same dimension 
#new matrix is what we will row reduce
#new matrix will have dimensions (M x 2M) for (M x M) input

