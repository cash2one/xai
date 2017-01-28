

#calss header
class _DOCTRINAL():
	def __init__(self,): 
		self.name = "DOCTRINAL"
		self.definitions = [u'relating to doctrine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
