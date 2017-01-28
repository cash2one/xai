

#calss header
class _CONCEITED():
	def __init__(self,): 
		self.name = "CONCEITED"
		self.definitions = [u'too proud of yourself and your actions and abilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
