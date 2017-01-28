

#calss header
class _STATESMANLIKE():
	def __init__(self,): 
		self.name = "STATESMANLIKE"
		self.definitions = [u'having or showing the qualities of a statesman: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
