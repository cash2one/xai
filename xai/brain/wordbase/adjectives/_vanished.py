

#calss header
class _VANISHED():
	def __init__(self,): 
		self.name = "VANISHED"
		self.definitions = [u'not now present or existing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
