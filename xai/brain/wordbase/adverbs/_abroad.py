

#calss header
class _ABROAD():
	def __init__(self,): 
		self.name = "ABROAD"
		self.definitions = [u'in or to a foreign country or countries: ', u'outside, or not at home: ', u'used to say that ideas, feelings, and opinions are shared by many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
