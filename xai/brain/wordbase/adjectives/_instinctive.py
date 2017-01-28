

#calss header
class _INSTINCTIVE():
	def __init__(self,): 
		self.name = "INSTINCTIVE"
		self.definitions = [u'Instinctive behaviour or reactions are not thought about, planned, or developed by training: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
