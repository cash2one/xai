

#calss header
class _HAPHAZARD():
	def __init__(self,): 
		self.name = "HAPHAZARD"
		self.definitions = [u'not having an obvious order or plan: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
