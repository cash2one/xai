

#calss header
class _ONEROUS():
	def __init__(self,): 
		self.name = "ONEROUS"
		self.definitions = [u'difficult to do or needing a lot of effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
