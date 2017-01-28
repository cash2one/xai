

#calss header
class _POSTDOCTORAL():
	def __init__(self,): 
		self.name = "POSTDOCTORAL"
		self.definitions = [u'relating to advanced work or study that someone does after completing their PhD: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
