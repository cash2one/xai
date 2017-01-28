

#calss header
class _PELLUCID():
	def __init__(self,): 
		self.name = "PELLUCID"
		self.definitions = [u'very clear and shining: ', u'very clear in meaning and easy to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
