

#calss header
class _BREECH():
	def __init__(self,): 
		self.name = "BREECH"
		self.definitions = [u'If a baby in the womb is in a breech position, it is lying so that the lower part of its body will come out first: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
