

#calss header
class _MUSLIM():
	def __init__(self,): 
		self.name = "MUSLIM"
		self.definitions = [u'Muslim people follow the religion of Islam: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
