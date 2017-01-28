

#calss header
class _AMORPHOUS():
	def __init__(self,): 
		self.name = "AMORPHOUS"
		self.definitions = [u'having no fixed form or shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
