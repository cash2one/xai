

#calss header
class _CULTIVATED():
	def __init__(self,): 
		self.name = "CULTIVATED"
		self.definitions = [u'Someone who is cultivated has had a good education and knows a lot about and likes art, music, painting, etc.', u'Cultivated land is used to grow crops: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
