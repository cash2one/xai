

#calss header
class _NEURAL():
	def __init__(self,): 
		self.name = "NEURAL"
		self.definitions = [u'involving a nerve or the system of nerves that includes the brain: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
