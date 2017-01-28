

#calss header
class _UNBRIDLED():
	def __init__(self,): 
		self.name = "UNBRIDLED"
		self.definitions = [u'not controlled or limited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
