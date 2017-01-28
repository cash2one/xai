

#calss header
class _EXCEPTIONABLE():
	def __init__(self,): 
		self.name = "EXCEPTIONABLE"
		self.definitions = [u'offensive or upsetting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
