

#calss header
class _ABUSIVE():
	def __init__(self,): 
		self.name = "ABUSIVE"
		self.definitions = [u'using rude and offensive words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
