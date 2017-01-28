

#calss header
class _SPLITTING():
	def __init__(self,): 
		self.name = "SPLITTING"
		self.definitions = [u'a very severe pain that you feel in your head']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
