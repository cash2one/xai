

#calss header
class _DARK():
	def __init__(self,): 
		self.name = "DARK"
		self.definitions = [u'with little or no light: ', u'nearer to black than white in colour: ', u'sad and without hope: ', u'evil or threatening: ', u'secret or hidden: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
