

#calss header
class _UNFOUNDED():
	def __init__(self,): 
		self.name = "UNFOUNDED"
		self.definitions = [u'If a claim or piece of news is unfounded, it is not based on fact: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
