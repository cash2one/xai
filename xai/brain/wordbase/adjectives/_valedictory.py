

#calss header
class _VALEDICTORY():
	def __init__(self,): 
		self.name = "VALEDICTORY"
		self.definitions = [u'relating to saying goodbye, especially formally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
