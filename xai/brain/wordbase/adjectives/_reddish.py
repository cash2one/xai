

#calss header
class _REDDISH():
	def __init__(self,): 
		self.name = "REDDISH"
		self.definitions = [u'slightly red in colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
