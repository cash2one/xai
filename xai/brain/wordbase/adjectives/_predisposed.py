

#calss header
class _PREDISPOSED():
	def __init__(self,): 
		self.name = "PREDISPOSED"
		self.definitions = [u'to be more likely than other people to have a medical condition or to behave in a particular way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
