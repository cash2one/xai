

#calss header
class _WHACKED():
	def __init__(self,): 
		self.name = "WHACKED"
		self.definitions = [u'very tired: ', u'suffering the effects of drugs or alcohol: ', u'strange or unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
