

#calss header
class _EASTERN():
	def __init__(self,): 
		self.name = "EASTERN"
		self.definitions = [u'in or from the east part of an area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
