

#calss header
class _ELABORATE():
	def __init__(self,): 
		self.name = "ELABORATE"
		self.definitions = [u'containing a lot of careful detail or many detailed parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
