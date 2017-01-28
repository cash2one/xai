

#calss header
class _PINCHED():
	def __init__(self,): 
		self.name = "PINCHED"
		self.definitions = [u'A pinched face is thin and pale: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
