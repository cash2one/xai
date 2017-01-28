

#calss header
class _STEAMY():
	def __init__(self,): 
		self.name = "STEAMY"
		self.definitions = [u'filled with steam, or hot and wet like steam: ', u'sexually exciting or including a lot of sexual activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
