

#calss header
class _MELANCHOLIC():
	def __init__(self,): 
		self.name = "MELANCHOLIC"
		self.definitions = [u'expressing feelings of sadness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
