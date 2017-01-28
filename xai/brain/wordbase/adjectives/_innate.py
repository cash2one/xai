

#calss header
class _INNATE():
	def __init__(self,): 
		self.name = "INNATE"
		self.definitions = [u'An innate quality or ability is one that you were born with, not one you have learned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
