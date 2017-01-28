

#calss header
class _PREDESTINED():
	def __init__(self,): 
		self.name = "PREDESTINED"
		self.definitions = [u'If an action or event is predestined, it is controlled by God or by fate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
