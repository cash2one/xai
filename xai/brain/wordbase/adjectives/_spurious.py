

#calss header
class _SPURIOUS():
	def __init__(self,): 
		self.name = "SPURIOUS"
		self.definitions = [u'false and not what it appears to be, or (of reasons and judgments) based on something that has not been correctly understood and therefore false: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
