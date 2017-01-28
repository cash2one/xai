

#calss header
class _WATERY():
	def __init__(self,): 
		self.name = "WATERY"
		self.definitions = [u'containing or filled with water: ', u'(of food or drink) containing too much water and therefore weak in taste: ', u'pale or weak in colour or strength: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
