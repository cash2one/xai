

#calss header
class _CRANIAL():
	def __init__(self,): 
		self.name = "CRANIAL"
		self.definitions = [u'of the skull']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
