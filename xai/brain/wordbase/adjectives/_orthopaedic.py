

#calss header
class _ORTHOPAEDIC():
	def __init__(self,): 
		self.name = "ORTHOPAEDIC"
		self.definitions = [u'relating to orthopaedics: ', u'designed to prevent or treat bone injuries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
