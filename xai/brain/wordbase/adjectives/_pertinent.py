

#calss header
class _PERTINENT():
	def __init__(self,): 
		self.name = "PERTINENT"
		self.definitions = [u'relating directly to the subject being considered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
