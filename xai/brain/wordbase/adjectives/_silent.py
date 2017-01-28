

#calss header
class _SILENT():
	def __init__(self,): 
		self.name = "SILENT"
		self.definitions = [u'without any sound: ', u'without talking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
