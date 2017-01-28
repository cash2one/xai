

#calss header
class _LESSER():
	def __init__(self,): 
		self.name = "LESSER"
		self.definitions = [u'used to describe something that is not as great in size, amount, or importance as something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
