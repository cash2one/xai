

#calss header
class _OVERHAND():
	def __init__(self,): 
		self.name = "OVERHAND"
		self.definitions = [u'(especially of a throw) made with the arm moving above the shoulder: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
