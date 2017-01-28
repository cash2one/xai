

#calss header
class _ECONOMICAL():
	def __init__(self,): 
		self.name = "ECONOMICAL"
		self.definitions = [u'not using a lot of fuel, money, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
