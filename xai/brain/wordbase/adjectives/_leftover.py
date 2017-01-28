

#calss header
class _LEFTOVER():
	def __init__(self,): 
		self.name = "LEFTOVER"
		self.definitions = [u'A leftover part of something is the part that has not been used or eaten when the other parts have been: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
