

#calss header
class _ABSORBENT():
	def __init__(self,): 
		self.name = "ABSORBENT"
		self.definitions = [u'able to take liquid in through the surface and to hold it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
