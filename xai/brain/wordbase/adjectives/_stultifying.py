

#calss header
class _STULTIFYING():
	def __init__(self,): 
		self.name = "STULTIFYING"
		self.definitions = [u'preventing new ideas from developing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
