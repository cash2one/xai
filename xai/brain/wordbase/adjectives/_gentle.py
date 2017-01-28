

#calss header
class _GENTLE():
	def __init__(self,): 
		self.name = "GENTLE"
		self.definitions = [u'calm, kind, or soft: ', u'not violent, severe, or strong: ', u'not steep or sudden: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
