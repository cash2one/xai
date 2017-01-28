

#calss header
class _VISUAL():
	def __init__(self,): 
		self.name = "VISUAL"
		self.definitions = [u'relating to seeing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
