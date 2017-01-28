

#calss header
class _INTEMPERATE():
	def __init__(self,): 
		self.name = "INTEMPERATE"
		self.definitions = [u'showing anger or violence that is too extreme and not well controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
