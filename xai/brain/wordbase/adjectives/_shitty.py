

#calss header
class _SHITTY():
	def __init__(self,): 
		self.name = "SHITTY"
		self.definitions = [u'unfair and unkind: ', u'bad, difficult, or unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
