

#calss header
class _COMPOSED():
	def __init__(self,): 
		self.name = "COMPOSED"
		self.definitions = [u'calm and in control of your emotions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
