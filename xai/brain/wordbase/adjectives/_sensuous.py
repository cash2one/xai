

#calss header
class _SENSUOUS():
	def __init__(self,): 
		self.name = "SENSUOUS"
		self.definitions = [u'giving or expressing pleasure through the physical senses, rather than pleasing the mind or the intelligence: ', u'\u2192\xa0 sensual : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
