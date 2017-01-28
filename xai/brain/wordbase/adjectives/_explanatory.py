

#calss header
class _EXPLANATORY():
	def __init__(self,): 
		self.name = "EXPLANATORY"
		self.definitions = [u'giving an explanation about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
