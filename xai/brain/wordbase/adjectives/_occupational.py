

#calss header
class _OCCUPATIONAL():
	def __init__(self,): 
		self.name = "OCCUPATIONAL"
		self.definitions = [u'relating to or caused by your job: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
