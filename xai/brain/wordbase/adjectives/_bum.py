

#calss header
class _BUM():
	def __init__(self,): 
		self.name = "BUM"
		self.definitions = [u'bad in quality or not useful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
