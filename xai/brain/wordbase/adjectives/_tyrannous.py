

#calss header
class _TYRANNOUS():
	def __init__(self,): 
		self.name = "TYRANNOUS"
		self.definitions = [u'using power or authority in a cruel and unfair way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
