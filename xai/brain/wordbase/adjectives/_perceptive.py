

#calss header
class _PERCEPTIVE():
	def __init__(self,): 
		self.name = "PERCEPTIVE"
		self.definitions = [u'very good at noticing and understanding things that many people do not notice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
