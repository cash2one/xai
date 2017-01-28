

#calss header
class _MARBLED():
	def __init__(self,): 
		self.name = "MARBLED"
		self.definitions = [u'decorated with a delicate pattern consisting of lines and areas of colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
