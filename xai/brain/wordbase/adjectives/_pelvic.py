

#calss header
class _PELVIC():
	def __init__(self,): 
		self.name = "PELVIC"
		self.definitions = [u'relating to the pelvis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
