

#calss header
class _PLATONIC():
	def __init__(self,): 
		self.name = "PLATONIC"
		self.definitions = [u'A platonic relationship or emotion is loving but not sexual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
