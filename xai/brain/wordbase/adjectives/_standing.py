

#calss header
class _STANDING():
	def __init__(self,): 
		self.name = "STANDING"
		self.definitions = [u'permanent, rather than formed or created when necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
