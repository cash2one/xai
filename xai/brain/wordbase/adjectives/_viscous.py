

#calss header
class _VISCOUS():
	def __init__(self,): 
		self.name = "VISCOUS"
		self.definitions = [u'A viscous liquid is thick and sticky and does not flow easily.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
