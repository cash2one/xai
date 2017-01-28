

#calss header
class _MARTIAL():
	def __init__(self,): 
		self.name = "MARTIAL"
		self.definitions = [u'relating to soldiers, war, or life in the armed forces']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
