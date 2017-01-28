

#calss header
class _STRESSFUL():
	def __init__(self,): 
		self.name = "STRESSFUL"
		self.definitions = [u'making you feel worried and nervous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
