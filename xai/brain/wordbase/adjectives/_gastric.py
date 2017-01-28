

#calss header
class _GASTRIC():
	def __init__(self,): 
		self.name = "GASTRIC"
		self.definitions = [u'relating to the stomach: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
