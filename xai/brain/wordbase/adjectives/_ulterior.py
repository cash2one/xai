

#calss header
class _ULTERIOR():
	def __init__(self,): 
		self.name = "ULTERIOR"
		self.definitions = [u'a secret purpose or reason for doing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
