

#calss header
class _INTRODUCTORY():
	def __init__(self,): 
		self.name = "INTRODUCTORY"
		self.definitions = [u'existing, used, or experienced for the first time: ', u'written or said at the beginning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
