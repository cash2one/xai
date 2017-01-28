

#calss header
class _DANK():
	def __init__(self,): 
		self.name = "DANK"
		self.definitions = [u'(especially of buildings and air) wet, cold, and unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
