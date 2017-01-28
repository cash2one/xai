

#calss header
class _ROBED():
	def __init__(self,): 
		self.name = "ROBED"
		self.definitions = [u'to be dressed in a particular way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
