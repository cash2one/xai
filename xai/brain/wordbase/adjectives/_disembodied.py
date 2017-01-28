

#calss header
class _DISEMBODIED():
	def __init__(self,): 
		self.name = "DISEMBODIED"
		self.definitions = [u'seeming not to have a body or not to be connected to a body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
