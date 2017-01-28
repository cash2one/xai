

#calss header
class _PITTED():
	def __init__(self,): 
		self.name = "PITTED"
		self.definitions = [u'covered with holes or low areas: ', u'with the pit (= seed) removed ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
