

#calss header
class _RUDE():
	def __init__(self,): 
		self.name = "RUDE"
		self.definitions = [u'not polite; offensive or embarrassing: ', u'relating to sex or going to the toilet: ', u'sudden and unpleasant: ', u'simply and roughly made: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
