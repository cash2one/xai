

#calss header
class _FLUSTERED():
	def __init__(self,): 
		self.name = "FLUSTERED"
		self.definitions = [u'upset and confused: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
