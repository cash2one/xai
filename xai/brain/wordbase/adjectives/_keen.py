

#calss header
class _KEEN():
	def __init__(self,): 
		self.name = "KEEN"
		self.definitions = [u'very interested, eager, or wanting (to do) something very much: ', u'extreme or very strong: ', u'very good or well developed: ', u'very sharp: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
