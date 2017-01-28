

#calss header
class _INCOHERENT():
	def __init__(self,): 
		self.name = "INCOHERENT"
		self.definitions = [u'expressing yourself in a way that is not clear: ', u'expressed in a way that is not clear, especially with words or ideas that are joined together badly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
