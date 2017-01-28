

#calss header
class _PROSTRATE():
	def __init__(self,): 
		self.name = "PROSTRATE"
		self.definitions = [u'lying with the face down and arms stretched out, especially as a sign of respect or worship', u'having lost all strength or all determination because of an illness or an extremely bad experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
