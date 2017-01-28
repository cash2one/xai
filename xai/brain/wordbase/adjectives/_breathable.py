

#calss header
class _BREATHABLE():
	def __init__(self,): 
		self.name = "BREATHABLE"
		self.definitions = [u'A breathable atmosphere is one that is suitable for humans to breathe.', u'Breathable fabrics for clothes allow air to pass through them. : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
