

#calss header
class _PRINCELY():
	def __init__(self,): 
		self.name = "PRINCELY"
		self.definitions = [u'used to refer to a surprisingly small amount of money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
