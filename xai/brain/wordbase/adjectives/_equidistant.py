

#calss header
class _EQUIDISTANT():
	def __init__(self,): 
		self.name = "EQUIDISTANT"
		self.definitions = [u'equally far or close: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
