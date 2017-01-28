

#calss header
class _ENTRENCHED():
	def __init__(self,): 
		self.name = "ENTRENCHED"
		self.definitions = [u'Entrenched ideas are so fixed or have existed for so long that they cannot be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
