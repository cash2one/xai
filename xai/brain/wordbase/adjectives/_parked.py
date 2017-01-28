

#calss header
class _PARKED():
	def __init__(self,): 
		self.name = "PARKED"
		self.definitions = [u'Parked vehicles have been left somewhere for a period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
