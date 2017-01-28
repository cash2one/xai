

#calss header
class _THRIFTY():
	def __init__(self,): 
		self.name = "THRIFTY"
		self.definitions = [u'showing a careful use of money, especially by avoiding waste: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
