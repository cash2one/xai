

#calss header
class _UNERRING():
	def __init__(self,): 
		self.name = "UNERRING"
		self.definitions = [u'never failing to hit a target', u'always accurate in your judgment or ability: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
