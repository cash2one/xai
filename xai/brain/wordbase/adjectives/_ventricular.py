

#calss header
class _VENTRICULAR():
	def __init__(self,): 
		self.name = "VENTRICULAR"
		self.definitions = [u'relating either to the ventricles of the heart or any space in the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
