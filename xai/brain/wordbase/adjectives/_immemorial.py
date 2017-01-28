

#calss header
class _IMMEMORIAL():
	def __init__(self,): 
		self.name = "IMMEMORIAL"
		self.definitions = [u'for a very long time: ', u'existing or traditional for an extremely long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
