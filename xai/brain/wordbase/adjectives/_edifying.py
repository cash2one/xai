

#calss header
class _EDIFYING():
	def __init__(self,): 
		self.name = "EDIFYING"
		self.definitions = [u'improving your mind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
