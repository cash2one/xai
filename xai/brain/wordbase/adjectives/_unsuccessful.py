

#calss header
class _UNSUCCESSFUL():
	def __init__(self,): 
		self.name = "UNSUCCESSFUL"
		self.definitions = [u'not achieving the hoped for result; not successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
