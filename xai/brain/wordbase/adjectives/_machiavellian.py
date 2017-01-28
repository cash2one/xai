

#calss header
class _MACHIAVELLIAN():
	def __init__(self,): 
		self.name = "MACHIAVELLIAN"
		self.definitions = [u'using clever but often dishonest methods that deceive people so that you can win power or control']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
