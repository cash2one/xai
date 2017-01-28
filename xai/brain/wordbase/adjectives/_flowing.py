

#calss header
class _FLOWING():
	def __init__(self,): 
		self.name = "FLOWING"
		self.definitions = [u'moving in one direction, especially continuously and easily: ', u'produced in a smooth, continuous, or relaxed style: ', u'Flowing hair and clothes are long and hang down loosely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
