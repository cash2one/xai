

#calss header
class _UNSPOKEN():
	def __init__(self,): 
		self.name = "UNSPOKEN"
		self.definitions = [u'not spoken, although thought of or felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
