

#calss header
class _RANDOM():
	def __init__(self,): 
		self.name = "RANDOM"
		self.definitions = [u'happening, done, or chosen by chance rather than according to a plan: ', u'strange or unusual: ', u'unknown and unexpected in a particular situation: ', u'by chance, or without being chosen intentionally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
