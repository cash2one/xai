

#calss header
class _LABOURED():
	def __init__(self,): 
		self.name = "LABOURED"
		self.definitions = [u'needing a lot of effort, often because someone is tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
