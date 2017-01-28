

#calss header
class _YOUNG():
	def __init__(self,): 
		self.name = "YOUNG"
		self.definitions = [u'having lived or existed for only a short time and not old: ', u'suitable for young people: ', u'to look younger than you really are']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
