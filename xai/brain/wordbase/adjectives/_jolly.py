

#calss header
class _JOLLY():
	def __init__(self,): 
		self.name = "JOLLY"
		self.definitions = [u'happy and smiling: ', u'enjoyable, energetic, and entertaining: ', u'bright and attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
