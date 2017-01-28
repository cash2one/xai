

#calss header
class _QUADRAPHONIC():
	def __init__(self,): 
		self.name = "QUADRAPHONIC"
		self.definitions = [u'(of an electronic system of recording, playing, or receiving sound) having sound coming from four different directions']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
