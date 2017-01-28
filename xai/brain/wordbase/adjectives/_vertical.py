

#calss header
class _VERTICAL():
	def __init__(self,): 
		self.name = "VERTICAL"
		self.definitions = [u'standing or pointing straight up or at an angle of 90\xb0 to a horizontal surface or line: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
