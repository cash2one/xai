

#calss header
class _LITTORAL():
	def __init__(self,): 
		self.name = "LITTORAL"
		self.definitions = [u'the part of a river, lake, or sea close to the land: ', u'near the coast: ', u'found in the littoral zone: ', u'used to refer to military ships that operate close to the land, or to their activities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
