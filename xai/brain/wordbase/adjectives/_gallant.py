

#calss header
class _GALLANT():
	def __init__(self,): 
		self.name = "GALLANT"
		self.definitions = [u'(of a man) polite and kind towards women, especially when in public: ', u'showing no fear of dangerous or difficult things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
