

#calss header
class _ABRASIVE():
	def __init__(self,): 
		self.name = "ABRASIVE"
		self.definitions = [u'rude and unfriendly: ', u'An abrasive substance is slightly rough, and often used for cleaning surfaces: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
