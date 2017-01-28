

#calss header
class _IMPOVERISHED():
	def __init__(self,): 
		self.name = "IMPOVERISHED"
		self.definitions = [u'very poor: ', u'made weaker or worse in quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
