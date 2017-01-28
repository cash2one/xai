

#calss header
class _PUGILISTIC():
	def __init__(self,): 
		self.name = "PUGILISTIC"
		self.definitions = [u'relating to boxing: ', u'wanting to fight or to hit someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
