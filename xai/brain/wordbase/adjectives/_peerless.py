

#calss header
class _PEERLESS():
	def __init__(self,): 
		self.name = "PEERLESS"
		self.definitions = [u'Something that is peerless is better than any other of its type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
