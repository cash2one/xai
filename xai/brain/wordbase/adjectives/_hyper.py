

#calss header
class _HYPER():
	def __init__(self,): 
		self.name = "HYPER"
		self.definitions = [u'too excited and energetic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
