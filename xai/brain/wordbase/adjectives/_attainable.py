

#calss header
class _ATTAINABLE():
	def __init__(self,): 
		self.name = "ATTAINABLE"
		self.definitions = [u'possible to achieve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
