

#calss header
class _MEMORABLE():
	def __init__(self,): 
		self.name = "MEMORABLE"
		self.definitions = [u'likely to be remembered or worth remembering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
