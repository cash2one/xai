

#calss header
class _COSTLY():
	def __init__(self,): 
		self.name = "COSTLY"
		self.definitions = [u'expensive, especially too expensive: ', u'involving a lot of loss or damage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
