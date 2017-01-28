

#calss header
class _ANTI():
	def __init__(self,): 
		self.name = "ANTI"
		self.definitions = [u'opposed to or against a particular thing or person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
