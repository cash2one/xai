

#calss header
class _INDISSOLUBLE():
	def __init__(self,): 
		self.name = "INDISSOLUBLE"
		self.definitions = [u'impossible to take apart or bring to an end, or existing for a very long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
