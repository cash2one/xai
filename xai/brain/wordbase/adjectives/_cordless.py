

#calss header
class _CORDLESS():
	def __init__(self,): 
		self.name = "CORDLESS"
		self.definitions = [u'A cordless electrical tool or piece of equipment operates without needing to be permanently connected by a wire to an electrical supply: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
