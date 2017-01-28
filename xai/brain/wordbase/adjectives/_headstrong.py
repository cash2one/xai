

#calss header
class _HEADSTRONG():
	def __init__(self,): 
		self.name = "HEADSTRONG"
		self.definitions = [u'very determined to do what you want without listening to others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
