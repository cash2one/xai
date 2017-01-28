

#calss header
class _JUDAIC():
	def __init__(self,): 
		self.name = "JUDAIC"
		self.definitions = [u'belonging or relating to Judaism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
