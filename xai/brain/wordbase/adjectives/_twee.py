

#calss header
class _TWEE():
	def __init__(self,): 
		self.name = "TWEE"
		self.definitions = [u'artificially attractive or too perfect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
