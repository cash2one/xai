

#calss header
class _TRANSCENDENTAL():
	def __init__(self,): 
		self.name = "TRANSCENDENTAL"
		self.definitions = [u'A transcendental experience, event, object, or idea is extremely special and unusual and cannot be understood in ordinary ways: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
