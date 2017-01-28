

#calss header
class _NASTY():
	def __init__(self,): 
		self.name = "NASTY"
		self.definitions = [u'bad or very unpleasant: ', u'unkind: ', u'dangerous or violent: ', u'rude or offensive: ', u'to think that something bad is likely to happen or to be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
