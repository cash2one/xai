

#calss header
class _STRICKEN():
	def __init__(self,): 
		self.name = "STRICKEN"
		self.definitions = [u'suffering severely from the effects of something unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
