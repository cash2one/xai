

#calss header
class _THEOLOGICAL():
	def __init__(self,): 
		self.name = "THEOLOGICAL"
		self.definitions = [u'relating to the study of religion and religious belief: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
