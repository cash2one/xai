

#calss header
class _COMPANIONABLE():
	def __init__(self,): 
		self.name = "COMPANIONABLE"
		self.definitions = [u'friendly and pleasant to be with']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
