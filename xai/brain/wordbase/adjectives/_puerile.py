

#calss header
class _PUERILE():
	def __init__(self,): 
		self.name = "PUERILE"
		self.definitions = [u'behaving in a silly way, not like an adult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
