

#calss header
class _MEDICAL():
	def __init__(self,): 
		self.name = "MEDICAL"
		self.definitions = [u'related to the treatment of illness and injuries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
