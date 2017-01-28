

#calss header
class _EVERGREEN():
	def __init__(self,): 
		self.name = "EVERGREEN"
		self.definitions = [u'An evergreen plant, bush, or tree has leaves for the whole year.', u'always seeming fresh or remaining popular: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
