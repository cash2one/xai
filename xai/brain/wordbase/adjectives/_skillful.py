

#calss header
class _SKILLFUL():
	def __init__(self,): 
		self.name = "SKILLFUL"
		self.definitions = [u'US spelling of  skilful ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
