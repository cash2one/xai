

#calss header
class _GENETIC():
	def __init__(self,): 
		self.name = "GENETIC"
		self.definitions = [u'belonging or relating to genes (= parts of the DNA in cells) received by each animal or plant from its parents: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
