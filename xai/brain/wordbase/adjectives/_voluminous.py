

#calss header
class _VOLUMINOUS():
	def __init__(self,): 
		self.name = "VOLUMINOUS"
		self.definitions = [u'A voluminous piece of clothing is large and consists of a lot of cloth: ', u'A voluminous piece of writing is long and detailed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
