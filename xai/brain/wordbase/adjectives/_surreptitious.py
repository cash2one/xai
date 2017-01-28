

#calss header
class _SURREPTITIOUS():
	def __init__(self,): 
		self.name = "SURREPTITIOUS"
		self.definitions = [u'done secretly, without anyone seeing or knowing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
