

#calss header
class _MESOLITHIC():
	def __init__(self,): 
		self.name = "MESOLITHIC"
		self.definitions = [u'relating to the middle part of the Stone Age (= the period when humans used tools and weapons made of stone): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
