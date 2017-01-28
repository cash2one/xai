

#calss header
class _IMPERISHABLE():
	def __init__(self,): 
		self.name = "IMPERISHABLE"
		self.definitions = [u'lasting for ever, or never becoming weaker with age']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
