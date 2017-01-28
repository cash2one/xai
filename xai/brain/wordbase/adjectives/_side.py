

#calss header
class _SIDE():
	def __init__(self,): 
		self.name = "SIDE"
		self.definitions = [u'not in or at the centre or main part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
