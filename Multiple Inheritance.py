class A:
 def feature1(self):
   print("Karthik")


class B:
 def feature2(self):
   print("Periyakaruppan")


class C(A,B):
 pass


obj=C()
obj.feature1()
