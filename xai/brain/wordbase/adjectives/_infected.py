

#calss header
class _INFECTED():
	def __init__(self,): 
		self.name = "INFECTED"
		self.definitions = [u'containing bacteria or other things that can cause disease: ', u'An infected computer file contains a computer virus (= a program that can harm computers and their files).']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
