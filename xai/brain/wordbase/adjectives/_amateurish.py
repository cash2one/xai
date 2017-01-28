

#calss header
class _AMATEURISH():
	def __init__(self,): 
		self.name = "AMATEURISH"
		self.definitions = [u'having no skill, or showing no skill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
