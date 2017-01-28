

#calss header
class _WANTED():
	def __init__(self,): 
		self.name = "WANTED"
		self.definitions = [u'wished for and loved by other people: ', u'being searched for by the police because of a crime: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
