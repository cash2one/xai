

#calss header
class _IRONCLAD():
	def __init__(self,): 
		self.name = "IRONCLAD"
		self.definitions = [u'very certain and unlikely to be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
