

#calss header
class _FEVERISH():
	def __init__(self,): 
		self.name = "FEVERISH"
		self.definitions = [u'suffering from fever (= high body temperature): ', u'unnaturally excited or active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
