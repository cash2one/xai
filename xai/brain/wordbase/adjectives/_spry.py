

#calss header
class _SPRY():
	def __init__(self,): 
		self.name = "SPRY"
		self.definitions = [u'(especially of older people) active and able to move quickly and energetically: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
