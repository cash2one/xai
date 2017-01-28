

#calss header
class _CONFIDENTIAL():
	def __init__(self,): 
		self.name = "CONFIDENTIAL"
		self.definitions = [u'secret, often in a formal, business, or military situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
