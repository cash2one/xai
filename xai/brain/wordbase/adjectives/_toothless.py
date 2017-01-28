

#calss header
class _TOOTHLESS():
	def __init__(self,): 
		self.name = "TOOTHLESS"
		self.definitions = [u'having no teeth: ', u'used to describe an organization or a rule that has no power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
