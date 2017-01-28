

#calss header
class _SEAWORTHY():
	def __init__(self,): 
		self.name = "SEAWORTHY"
		self.definitions = [u'(of a ship) in a condition that is good enough to travel safely on the sea']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
