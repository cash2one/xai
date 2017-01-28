

#calss header
class _HARMONIOUS():
	def __init__(self,): 
		self.name = "HARMONIOUS"
		self.definitions = [u'having a pleasant tune or harmony', u'friendly and peaceful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
