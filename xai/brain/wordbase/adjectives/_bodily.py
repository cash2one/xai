

#calss header
class _BODILY():
	def __init__(self,): 
		self.name = "BODILY"
		self.definitions = [u'relating to the human body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
