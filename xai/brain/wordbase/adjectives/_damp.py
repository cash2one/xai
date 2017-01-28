

#calss header
class _DAMP():
	def __init__(self,): 
		self.name = "DAMP"
		self.definitions = [u'slightly wet, especially in a way that is not pleasant or comfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
