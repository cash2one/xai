

#calss header
class _LINGERING():
	def __init__(self,): 
		self.name = "LINGERING"
		self.definitions = [u'lasting a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
