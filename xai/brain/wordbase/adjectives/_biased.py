

#calss header
class _BIASED():
	def __init__(self,): 
		self.name = "BIASED"
		self.definitions = [u'showing an unreasonable like or dislike for a person based on personal opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
