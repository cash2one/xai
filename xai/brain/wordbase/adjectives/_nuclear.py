

#calss header
class _NUCLEAR():
	def __init__(self,): 
		self.name = "NUCLEAR"
		self.definitions = [u'being or using the power produced when the nucleus of an atom is divided or joined to another nucleus: ', u'relating to weapons, or the use of weapons, which use the power produced when the nucleus of an atom is divided or joined to another nucleus: ', u'relating to the nucleus of an atom: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
