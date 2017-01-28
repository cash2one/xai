

#calss header
class _GEOGRAPHICAL():
	def __init__(self,): 
		self.name = "GEOGRAPHICAL"
		self.definitions = [u'relating to geography, or to the geography of a particular area or place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
