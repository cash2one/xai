

#calss header
class _UNACCUSTOMED():
	def __init__(self,): 
		self.name = "UNACCUSTOMED"
		self.definitions = [u'not familiar with something, or not used to something: ', u'not usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
