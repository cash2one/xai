

#calss header
class _UNABASHED():
	def __init__(self,): 
		self.name = "UNABASHED"
		self.definitions = [u'without any worry about possible criticism or embarrassment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
