

#calss header
class _DIVORCED():
	def __init__(self,): 
		self.name = "DIVORCED"
		self.definitions = [u'married in the past but not now married: ', u'not based on or affected by something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
