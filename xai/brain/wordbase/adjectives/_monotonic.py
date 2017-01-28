

#calss header
class _MONOTONIC():
	def __init__(self,): 
		self.name = "MONOTONIC"
		self.definitions = [u'speaking or spoken in such a way that the sound stays on the same note without going higher or lower', u'(of a quantity) only ever increasing, or only ever getting less']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
