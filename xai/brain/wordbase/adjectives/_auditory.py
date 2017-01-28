

#calss header
class _AUDITORY():
	def __init__(self,): 
		self.name = "AUDITORY"
		self.definitions = [u'of or about hearing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
