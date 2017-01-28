

#calss header
class _FERTILE():
	def __init__(self,): 
		self.name = "FERTILE"
		self.definitions = [u'Fertile land can produce a large number of good quality crops.', u'Fertile animals or plants are able to produce (a lot of) young or fruit: ', u'A fertile seed or egg is able to develop into a new plant or animal.', u'A fertile mind or imagination is active and produces a lot of interesting and unusual ideas.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
