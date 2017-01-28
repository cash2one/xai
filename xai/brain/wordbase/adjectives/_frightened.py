

#calss header
class _FRIGHTENED():
	def __init__(self,): 
		self.name = "FRIGHTENED"
		self.definitions = [u'feeling fear or worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
