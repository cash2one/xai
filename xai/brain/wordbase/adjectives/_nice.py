

#calss header
class _NICE():
	def __init__(self,): 
		self.name = "NICE"
		self.definitions = [u'pleasant, enjoyable, or satisfactory: ', u'pleasantly: ', u'kind, friendly, or polite: ', u'based on very slight differences: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
