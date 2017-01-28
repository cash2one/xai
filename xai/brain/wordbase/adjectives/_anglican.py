

#calss header
class _ANGLICAN():
	def __init__(self,): 
		self.name = "ANGLICAN"
		self.definitions = [u'relating to the Church of England, or an international Church connected with it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
