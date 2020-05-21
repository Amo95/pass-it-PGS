import  random

class PassLength:
	def __init__(self, string):
		self.string = string
		self.num =  [i for i in range(8, 33, 8)][::-1]

	def eight(self):
		return "".join(random.sample(self.string, self.num[-1]))

	def sixteen(self):
		return "".join(random.sample(self.string, self.num.pop(1)))

	def twenty(self):
		return "".join(random.sample(self.string, self.num[1]))

	def thirty(self):
		print(self.num)
		return "".join(random.sample(self.string, self.num[0]))

	def manual(self, lens):
		if len(str(lens)) <= 104:
			return "".join(random.sample(self.string, lens))
		else:
			return