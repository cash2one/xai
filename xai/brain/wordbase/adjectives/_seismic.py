

#calss header
class _SEISMIC():
	def __init__(self,): 
		self.name = "SEISMIC"
		self.definitions = [u'relating to or caused by an earthquake: ', u'having very great and damaging effects: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
