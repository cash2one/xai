

#calss header
class _HEINOUS():
	def __init__(self,): 
		self.name = "HEINOUS"
		self.definitions = [u'very bad and shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
