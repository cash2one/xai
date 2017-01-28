

#calss header
class _SCHOLARLY():
	def __init__(self,): 
		self.name = "SCHOLARLY"
		self.definitions = [u'containing a serious, detailed study of a subject: ', u'A scholarly person studies a lot and knows a lot about what they study: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
