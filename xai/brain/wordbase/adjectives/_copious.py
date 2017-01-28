

#calss header
class _COPIOUS():
	def __init__(self,): 
		self.name = "COPIOUS"
		self.definitions = [u'in large amounts, or more than enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
