

#calss header
class _DOGMATIC():
	def __init__(self,): 
		self.name = "DOGMATIC"
		self.definitions = [u'If you are dogmatic, you are certain that you are right and that everyone else is wrong.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
