# Python program to demonstrate
# hybrid inheritance


class A:
	def dA(self):
		print("class A")

class B(A):
	def dB(self):
		print("class B ")

class C(A):
	def dC(self):
		print("class C")

class D(B, A):
	def dD(self):
		print("class D")

# Driver's code
object = D()
object.dA()
object.dB()

