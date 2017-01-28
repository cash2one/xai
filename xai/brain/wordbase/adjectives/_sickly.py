

#calss header
class _SICKLY():
	def __init__(self,): 
		self.name = "SICKLY"
		self.definitions = [u'weak, unhealthy, and often sick: ', u'causing a slight feeling of wanting to vomit: ', u'emotional, in an unpleasant or embarrassing way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
