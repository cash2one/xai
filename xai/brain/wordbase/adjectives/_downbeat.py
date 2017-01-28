

#calss header
class _DOWNBEAT():
	def __init__(self,): 
		self.name = "DOWNBEAT"
		self.definitions = [u'quiet and without much excitement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
