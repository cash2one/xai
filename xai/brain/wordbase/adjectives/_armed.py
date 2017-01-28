

#calss header
class _ARMED():
	def __init__(self,): 
		self.name = "ARMED"
		self.definitions = [u'using or carrying weapons: ', u'carrying many weapons: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
