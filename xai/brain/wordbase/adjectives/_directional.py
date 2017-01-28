

#calss header
class _DIRECTIONAL():
	def __init__(self,): 
		self.name = "DIRECTIONAL"
		self.definitions = [u'Directional radio equipment receives or sends stronger signals in particular directions.', u'very fashionable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
