

#calss header
class _UNINSURED():
	def __init__(self,): 
		self.name = "UNINSURED"
		self.definitions = [u'not having any insurance to pay for medical expenses or for damage or injury while driving a car: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
