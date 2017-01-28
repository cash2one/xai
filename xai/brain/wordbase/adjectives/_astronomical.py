

#calss header
class _ASTRONOMICAL():
	def __init__(self,): 
		self.name = "ASTRONOMICAL"
		self.definitions = [u'connected with astronomy: ', u'An astronomical amount is extremely large: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
