

#calss header
class _IMPASSIVE():
	def __init__(self,): 
		self.name = "IMPASSIVE"
		self.definitions = [u"If someone's face is impassive, it expresses no emotion, because the person seems not to be affected by the situation they are experiencing."]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
