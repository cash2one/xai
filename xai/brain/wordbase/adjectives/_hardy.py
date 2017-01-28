

#calss header
class _HARDY():
	def __init__(self,): 
		self.name = "HARDY"
		self.definitions = [u'strong enough to bear extreme conditions or difficult situations: ', u'Hardy plants can live through the winter without protection from the weather: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
