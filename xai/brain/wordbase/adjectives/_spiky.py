

#calss header
class _SPIKY():
	def __init__(self,): 
		self.name = "SPIKY"
		self.definitions = [u'covered with spikes or having that appearance: ', u'easily annoyed and not polite: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
