

#calss header
class _INTIMIDATING():
	def __init__(self,): 
		self.name = "INTIMIDATING"
		self.definitions = [u'making you feel frightened or nervous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
