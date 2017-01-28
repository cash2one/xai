

#calss header
class _UNPLEASANT():
	def __init__(self,): 
		self.name = "UNPLEASANT"
		self.definitions = [u'not enjoyable or pleasant: ', u'rude and angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
