

#calss header
class _IAMBIC():
	def __init__(self,): 
		self.name = "IAMBIC"
		self.definitions = [u'used to refer to a rhythm (= pattern of words) used in poetry, in which each short syllable that is not stressed is followed by a long or stressed syllable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
