

#calss header
class _SHODDY():
	def __init__(self,): 
		self.name = "SHODDY"
		self.definitions = [u'badly and carelessly made, using low quality materials: ', u'showing little respect, thought, or care: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
