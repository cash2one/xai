

#calss header
class _MISBEGOTTEN():
	def __init__(self,): 
		self.name = "MISBEGOTTEN"
		self.definitions = [u'badly or stupidly planned or designed: ', u'not deserving to be respected or thought valuable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
