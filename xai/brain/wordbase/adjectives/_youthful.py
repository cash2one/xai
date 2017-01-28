

#calss header
class _YOUTHFUL():
	def __init__(self,): 
		self.name = "YOUTHFUL"
		self.definitions = [u'having the qualities that are typical of young people: ', u'young: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
