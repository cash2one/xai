

#calss header
class _DECISIVE():
	def __init__(self,): 
		self.name = "DECISIVE"
		self.definitions = [u'able to make decisions quickly and confidently, or showing this quality: ', u'strongly affecting how a situation will progress or end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
