

#calss header
class _CORONARY():
	def __init__(self,): 
		self.name = "CORONARY"
		self.definitions = [u'relating to the arteries (= thick tubes) that supply blood to the muscles of the heart: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
