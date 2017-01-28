

#calss header
class _SCABROUS():
	def __init__(self,): 
		self.name = "SCABROUS"
		self.definitions = [u'offensive or shocking, because describing or showing sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
