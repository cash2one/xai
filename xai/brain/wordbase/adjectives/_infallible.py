

#calss header
class _INFALLIBLE():
	def __init__(self,): 
		self.name = "INFALLIBLE"
		self.definitions = [u'never wrong, failing, or making a mistake: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
