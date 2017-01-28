

#calss header
class _UNETHICAL():
	def __init__(self,): 
		self.name = "UNETHICAL"
		self.definitions = [u'not ethical (= based on moral beliefs)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
