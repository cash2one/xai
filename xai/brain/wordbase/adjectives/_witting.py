

#calss header
class _WITTING():
	def __init__(self,): 
		self.name = "WITTING"
		self.definitions = [u'knowing what is involved in a particular situation; done while being aware of the facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
