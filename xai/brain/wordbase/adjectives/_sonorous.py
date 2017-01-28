

#calss header
class _SONOROUS():
	def __init__(self,): 
		self.name = "SONOROUS"
		self.definitions = [u'having a deep, pleasant sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
