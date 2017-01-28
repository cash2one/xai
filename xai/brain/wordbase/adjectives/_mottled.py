

#calss header
class _MOTTLED():
	def __init__(self,): 
		self.name = "MOTTLED"
		self.definitions = [u'covered with areas of different colours that do not form a regular pattern: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
