

#calss header
class _ABLAZE():
	def __init__(self,): 
		self.name = "ABLAZE"
		self.definitions = [u'burning very strongly: ', u'brightly lit or brightly coloured: ', u'full of energy, interest, or emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
