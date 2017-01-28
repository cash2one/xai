

#calss header
class _MARSUPIAL():
	def __init__(self,): 
		self.name = "MARSUPIAL"
		self.definitions = [u"giving birth to young that are not completely developed when they are born, and that are carried and fed in a pouch on the mother's body: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
