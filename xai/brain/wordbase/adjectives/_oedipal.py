

#calss header
class _OEDIPAL():
	def __init__(self,): 
		self.name = "OEDIPAL"
		self.definitions = [u'relating to an Oedipus complex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
