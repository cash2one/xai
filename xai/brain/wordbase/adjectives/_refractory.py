

#calss header
class _REFRACTORY():
	def __init__(self,): 
		self.name = "REFRACTORY"
		self.definitions = [u'not affected by a treatment, change, or process: ', u'difficult to control; unwilling to obey: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
