

#calss header
class _RETROGRADE():
	def __init__(self,): 
		self.name = "RETROGRADE"
		self.definitions = [u'returning to older and worse conditions, methods, ideas, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
