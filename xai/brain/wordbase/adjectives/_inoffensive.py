

#calss header
class _INOFFENSIVE():
	def __init__(self,): 
		self.name = "INOFFENSIVE"
		self.definitions = [u'not causing any harm or offence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
