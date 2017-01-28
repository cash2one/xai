

#calss header
class _DETACHED():
	def __init__(self,): 
		self.name = "DETACHED"
		self.definitions = [u'separated: ', u'A detached house is not connected to any other building: ', u'A detached person does not show any emotional involvement or interest in a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
