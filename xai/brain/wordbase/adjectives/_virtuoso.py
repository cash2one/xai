

#calss header
class _VIRTUOSO():
	def __init__(self,): 
		self.name = "VIRTUOSO"
		self.definitions = [u'extremely skilled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
