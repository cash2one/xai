

#calss header
class _SPINAL():
	def __init__(self,): 
		self.name = "SPINAL"
		self.definitions = [u'of the spine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
