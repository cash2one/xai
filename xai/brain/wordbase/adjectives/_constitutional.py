

#calss header
class _CONSTITUTIONAL():
	def __init__(self,): 
		self.name = "CONSTITUTIONAL"
		self.definitions = [u'allowed by or contained in a constitution: ', u"relating to someone's general state of health: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
