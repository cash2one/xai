

#calss header
class _DOLEFUL():
	def __init__(self,): 
		self.name = "DOLEFUL"
		self.definitions = [u'very sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
