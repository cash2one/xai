

#calss header
class _GRASPING():
	def __init__(self,): 
		self.name = "GRASPING"
		self.definitions = [u'(of people) always trying to get and keep more of something, especially money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
