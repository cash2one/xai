

#calss header
class _PSYCHOSOMATIC():
	def __init__(self,): 
		self.name = "PSYCHOSOMATIC"
		self.definitions = [u'(of an illness) caused by anxiety and worry and not by an infection or injury: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
