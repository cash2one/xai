

#calss header
class _MAXIMUM():
	def __init__(self,): 
		self.name = "MAXIMUM"
		self.definitions = [u'being the largest amount or number allowed or possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
