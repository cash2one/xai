

#calss header
class _NOISY():
	def __init__(self,): 
		self.name = "NOISY"
		self.definitions = [u'making a lot of noise: ', u'having an unwanted change in signal, especially of an electronic device: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
