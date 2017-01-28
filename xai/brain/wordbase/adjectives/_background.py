

#calss header
class _BACKGROUND():
	def __init__(self,): 
		self.name = "BACKGROUND"
		self.definitions = [u'used to refer to something that is done before, and in preparation for, something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
