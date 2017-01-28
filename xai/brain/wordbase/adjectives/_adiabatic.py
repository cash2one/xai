

#calss header
class _ADIABATIC():
	def __init__(self,): 
		self.name = "ADIABATIC"
		self.definitions = [u'an adiabatic process is one in which there is no heat transfer (= heat does not enter or leave the system)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
