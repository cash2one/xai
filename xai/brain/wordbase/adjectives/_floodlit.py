

#calss header
class _FLOODLIT():
	def __init__(self,): 
		self.name = "FLOODLIT"
		self.definitions = [u'lit by floodlights: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
