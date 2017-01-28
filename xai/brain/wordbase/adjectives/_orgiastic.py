

#calss header
class _ORGIASTIC():
	def __init__(self,): 
		self.name = "ORGIASTIC"
		self.definitions = [u'An orgiastic activity involves wild, uncontrolled behaviour and feelings of great pleasure and excitement.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
