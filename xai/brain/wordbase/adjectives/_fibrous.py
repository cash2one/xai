

#calss header
class _FIBROUS():
	def __init__(self,): 
		self.name = "FIBROUS"
		self.definitions = [u'made of fibres, or like fibre', u'Food that is fibrous contains fibre.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
