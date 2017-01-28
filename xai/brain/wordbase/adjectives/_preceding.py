

#calss header
class _PRECEDING():
	def __init__(self,): 
		self.name = "PRECEDING"
		self.definitions = [u'existing or happening before someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
