

#calss header
class _MELANCHOLY():
	def __init__(self,): 
		self.name = "MELANCHOLY"
		self.definitions = [u'sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
