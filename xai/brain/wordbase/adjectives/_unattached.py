

#calss header
class _UNATTACHED():
	def __init__(self,): 
		self.name = "UNATTACHED"
		self.definitions = [u'not married or not having a relationship with anyone; single: ', u'not physically joined to something else: ', u'not feeling connected to a person, group, or idea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
