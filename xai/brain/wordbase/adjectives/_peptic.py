

#calss header
class _PEPTIC():
	def __init__(self,): 
		self.name = "PEPTIC"
		self.definitions = [u'relating to pepsin (= an enzyme in the stomach that is involved in breaking down proteins): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
