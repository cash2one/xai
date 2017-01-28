

#calss header
class _HELLENIC():
	def __init__(self,): 
		self.name = "HELLENIC"
		self.definitions = [u'of or relating to the ancient or modern Greeks, and their history, art, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
