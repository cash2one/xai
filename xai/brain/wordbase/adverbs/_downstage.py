

#calss header
class _DOWNSTAGE():
	def __init__(self,): 
		self.name = "DOWNSTAGE"
		self.definitions = [u'towards or at the front of the stage in a theatre']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
